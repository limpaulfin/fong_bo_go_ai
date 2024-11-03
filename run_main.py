"""
Bộ Gõ AI - Công cụ hỗ trợ gõ văn bản thông minh với AI

Chức năng chính:
- Theo dõi và sửa lỗi văn bản real-time
- Hỗ trợ đa ngôn ngữ (VN, EN)
- Tự động thống kê token usage
- Xử lý thông minh với context

Cách hoạt động:
1. Theo dõi keyboard input
2. Kích hoạt bằng double space hoặc scroll lock
3. Lấy văn bản từ vị trí con trỏ đến đầu dòng
4. Gửi API để sửa lỗi
5. Thay thế văn bản cũ bằng văn bản đã sửa

Author: [Lam Thanh Phong]
Version: 1.0.0
"""

import time
from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
from openai import OpenAI
import os
from dotenv import load_dotenv
import json
import re
import threading
from datetime import datetime
from PIL import Image
import pystray
import signal
import sys

# Load environment variables
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

keyboard_controller = Controller()
should_scan = False
last_space_time = 0
space_count = 0
DOUBLE_SPACE_THRESHOLD = 0.2
TEMPERATURE = 0.5

is_calling_api = False

# Constants cho file paths
LOG_FOLDER = "logs"
MY_PROMPT = os.path.join("my_prompt.md")
API_LOG_FILE = os.path.join(LOG_FOLDER, "api_responses.jsonl")
TOKEN_STATS_FILE = os.path.join(LOG_FOLDER, "token_stats.json")

# Tạo thư mục logs nếu chưa tồn tại
if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)

class TokenUsageTracker:
    def __init__(self, stats_file):
        self.stats_file = stats_file
        self.stats = self._load_stats()

    def _load_stats(self):
        if os.path.exists(self.stats_file):
            try:
                with open(self.stats_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return self._create_default_stats()
        return self._create_default_stats()

    def _create_default_stats(self):
        return {
            "total_tokens": 0,
            "daily_tokens": {},
            "monthly_tokens": {}
        }

    def _save_stats(self):
        with open(self.stats_file, 'w', encoding='utf-8') as f:
            json.dump(self.stats, f, indent=2, ensure_ascii=False)

    def update_usage(self, tokens):
        today = datetime.now().strftime("%Y-%m-%d")
        month = datetime.now().strftime("%Y-%m")

        # Cập nhật tổng token
        self.stats["total_tokens"] += tokens

        # Cập nhật token theo ngày
        if today not in self.stats["daily_tokens"]:
            self.stats["daily_tokens"][today] = 0
        self.stats["daily_tokens"][today] += tokens

        # Cập nhật token theo tháng
        if month not in self.stats["monthly_tokens"]:
            self.stats["monthly_tokens"][month] = 0
        self.stats["monthly_tokens"][month] += tokens

        self._save_stats()

    def get_stats(self):
        today = datetime.now().strftime("%Y-%m-%d")
        month = datetime.now().strftime("%Y-%m")
        return {
            "total_tokens": self.stats["total_tokens"],
            "today_tokens": self.stats["daily_tokens"].get(today, 0),
            "month_tokens": self.stats["monthly_tokens"].get(month, 0)
        }

# Khởi tạo TokenUsageTracker sau khi đã định nghĩa class
token_tracker = TokenUsageTracker(TOKEN_STATS_FILE)

def show_api_status():
    """
    Hiển thị trạng thái đang gọi API bằng cách thêm 3 dấu chấm
    """
    global is_calling_api
    if is_calling_api:
        keyboard_controller.type('...')

def clear_api_status():
    """
    Xóa trạng thái API bằng cách xóa 3 dấu chấm
    """
    for _ in range(3):
        keyboard_controller.press(Key.backspace)
        keyboard_controller.release(Key.backspace)
        time.sleep(0.01)

def read_context():
    """
    Đọc nội dung từ file my_context.md

    Returns:
        str: Nội dung của file context, hoặc chuỗi rỗng nếu có lỗi
    """
    try:
        if os.path.exists(MY_PROMPT):
            with open(MY_PROMPT, 'r', encoding='utf-8') as f:
                return f.read().strip()
        return ""
    except Exception as e:
        print(f"Lỗi khi đọc context: {str(e)}")
        return ""

def get_correction(text):
    """
    Gửi văn bản đến OpenAI API để sửa lỗi

    Args:
        text (str): Văn bản cần sửa

    Returns:
        str: Văn bản đã được sửa
    """
    global is_calling_api
    try:
        is_calling_api = True
        status_thread = threading.Thread(target=show_api_status)
        status_thread.daemon = True
        status_thread.start()

        # Đọc context từ file
        context = read_context()

        prompt = f"""

        {context}

        Format:
        - json, nằm trong dấu ```json
        - cấu trúc của json trả về phải có cấu trúc như sau (đây chỉ là ví dụ):
            {{
                \"correction\": \"[văn bản được sửa]\"
            }}

        Input: \"\"\" {text} \"\"\"
        """

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Bạn là một hệ thống sửa lỗi văn bản cực kỳ thông minh và tiên tiến."},
                {"role": "user", "content": prompt}
            ],
            temperature=TEMPERATURE,
        )

        # Sau khi có kết quả
        is_calling_api = False
        status_thread.join(timeout=1.0)
        # Xóa dấu ...
        clear_api_status()

        # Debug: In ra response từ API để kiểm tra
        #print("\nAPI Response raw:", completion.choices[0].message.content)
        response = completion.choices[0].message.content.strip()
        print("Response after strip:", response)

        # Xử lý JSON response mới
        try:
            # Loại b các ký tự markdown ```json và ```
            json_text = re.sub(r'^```json\s*|\s*```$', '', response.strip())
            # Parse JSON
            result = json.loads(json_text)
            corrected_text = result.get("correction", text)

            # Log API response và cập nhật token usage
            log_api_response(completion, text, corrected_text)
            token_tracker.update_usage(completion.usage.total_tokens)

            # In thống kê token
            stats = token_tracker.get_stats()
            print("\nThống kê token:")
            print(f"- Tổng token đã dùng: {stats['total_tokens']:,}")
            print(f"- Token hôm nay: {stats['today_tokens']:,}")
            print(f"- Token tháng này: {stats['month_tokens']:,}")

            return corrected_text
        except json.JSONDecodeError as e:
            print(f"Lỗi khi phân tích JSON: {str(e)}")
            return text
    except Exception as e:
        is_calling_api = False
        clear_api_status()  # Đảm bảo xóa dấu ... khi có lỗi
        print(f"Lỗi khi gọi API: {str(e)}")
        return text

def get_selected_text():
    """
    Lấy văn bản ược chọn hoặc văn bản từ vị trí hiện tại đến đầu dòng

    Returns:
        tuple: (selected_text, has_selection)
            - selected_text (str): Văn bản được chọn
            - has_selection (bool): True nếu có selection sẵn
    """
    original = pyperclip.paste()  # Lưu clipboard gốc
    has_selection = False
    selected_text = ""

    try:
        # Thử lấy selection hiện tại (nếu có)
        with keyboard_controller.pressed(Key.ctrl):
            keyboard_controller.tap('c')
        time.sleep(0.1)

        selected_text = pyperclip.paste()
        has_selection = selected_text != original and selected_text.strip() != ""

        if not has_selection:
            # Select từ vị trí hiện tại đến đầu dòng
            keyboard_controller.press(Key.shift)
            keyboard_controller.press(Key.home)
            keyboard_controller.release(Key.home)
            keyboard_controller.release(Key.shift)
            time.sleep(0.1)

            # Copy với retry
            max_retries = 3
            for _ in range(max_retries):
                with keyboard_controller.pressed(Key.ctrl):
                    keyboard_controller.tap('c')
                time.sleep(0.1)

                selected_text = pyperclip.paste()
                if selected_text and selected_text != original:
                    break
                time.sleep(0.1)

            # Hủy selection
            keyboard_controller.tap(Key.right)

        return selected_text, has_selection

    except Exception as e:
        print(f"Lỗi khi lấy text: {str(e)}")
        return "", False

    finally:
        # Đảm bảo luôn restore clipboard sau 1 khoảng thời gian
        time.sleep(0.1)
        pyperclip.copy(original)

def replace_current_line(new_text, has_selection):
    original = pyperclip.paste()
    max_retries = 3

    try:
        # Copy new_text vào clipboard
        for _ in range(max_retries):
            pyperclip.copy(new_text)
            time.sleep(0.1)
            if pyperclip.paste() == new_text:
                break

        if has_selection:
            # Paste vào vùng đã select
            with keyboard_controller.pressed(Key.ctrl):
                keyboard_controller.tap('v')
            time.sleep(0.1)
        else:
            # Select từ vị trí hiện tại đến đầu dòng
            keyboard_controller.press(Key.shift)
            keyboard_controller.press(Key.home)
            keyboard_controller.release(Key.home)
            keyboard_controller.release(Key.shift)
            time.sleep(0.1)

            # Paste text mới
            with keyboard_controller.pressed(Key.ctrl):
                keyboard_controller.tap('v')
            time.sleep(0.1)

            # Di chuyển con trỏ về cuối
            keyboard_controller.tap(Key.end)

    finally:
        # Restore clipboard gốc
        time.sleep(0.2)
        for _ in range(max_retries):
            pyperclip.copy(original)
            if pyperclip.paste() == original:
                break
            time.sleep(0.1)

def on_press(key):
    global should_scan, last_space_time, space_count
    try:
        # Xử lý Double Right Shift
        if key == Key.shift_r:
            current_time = time.time()
            time_diff = current_time - last_space_time

            if time_diff < DOUBLE_SPACE_THRESHOLD:
                space_count += 1
                if space_count == 2:
                    should_scan = True
                    space_count = 0
            else:
                space_count = 1

            last_space_time = current_time

        # Xử lý Double Space
        elif key == Key.space or (isinstance(key, keyboard.KeyCode) and key.char == ' '):
            current_time = time.time()
            time_diff = current_time - last_space_time

            if time_diff < DOUBLE_SPACE_THRESHOLD:
                space_count += 1
                if space_count == 2:
                    should_scan = True
                    space_count = 0
            else:
                space_count = 1

            last_space_time = current_time
        else:
            if space_count > 0:
                space_count = 0

    except AttributeError:
        pass

def log_api_response(response_data, text_input, corrected_output):
    """
    Ghi log API response với format JSONL (mỗi dòng là một JSON object)
    """
    timestamp = datetime.now().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "input": text_input,
        "output": corrected_output,
        "response_id": response_data.id,
        "model": response_data.model,
        "system_fingerprint": response_data.system_fingerprint,
        "usage": {
            "prompt_tokens": response_data.usage.prompt_tokens,
            "completion_tokens": response_data.usage.completion_tokens,
            "total_tokens": response_data.usage.total_tokens
        },
        "finish_reason": response_data.choices[0].finish_reason
    }

    try:
        with open(API_LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + '\n')
    except Exception as e:
        print(f"Lỗi khi ghi API log: {str(e)}")

# Thêm hàm mới để log context
def log_context(text):
    """
    Ghi log context để training AI trong tương lai
    """
    try:
        with open(MY_PROMPT, "a", encoding="utf-8") as f:
            f.write(f"{text}\n")
    except Exception as e:
        print(f"Lỗi khi ghi context log: {str(e)}")

# Thêm biến global để lưu clipboard gốc
original_clipboard = None

def save_clipboard():
    """
    Lưu nội dung clipboard hiện tại
    """
    global original_clipboard
    try:
        original_clipboard = pyperclip.paste()
    except Exception as e:
        print(f"Lỗi khi lưu clipboard: {str(e)}")
        original_clipboard = ''

def restore_clipboard():
    """
    Khôi phục nội dung clipboard đã lưu
    """
    global original_clipboard
    if original_clipboard is not None:
        try:
            pyperclip.copy(original_clipboard)
        except Exception as e:
            print(f"Lỗi khi khôi phục clipboard: {str(e)}")

# Thêm code sau phần imports và trước khi khởi tạo các biến
def create_tray_icon():
    """
    Tạo system tray icon với menu context
    """
    def on_quit(icon):
        """Xử lý thoát script"""
        icon.stop()
        os._exit(0)

    def restart_script(icon):
        """Khởi động lại script"""
        icon.stop()
        # Lấy đường dẫn tới script hiện tại
        script_path = os.path.abspath(__file__)
        # Khởi động lại script bằng pythonw
        if os.name == 'nt':  # Windows
            os.system(f'start pythonw "{script_path}"')
        else:  # Linux/Mac
            os.system(f'python3 "{script_path}" &')
        # Thoát script hiện tại
        os._exit(0)

    def open_source_location(icon):
        """Mở thư mục chứa file mã nguồn"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.startfile(script_dir) if os.name == 'nt' else os.system(f'xdg-open "{script_dir}"')

    # Load icon image
    try:
        image = Image.open("icon.png")
    except Exception as e:
        print(f"Lỗi khi load icon: {str(e)}")
        # Tạo icon mặc định nếu không load được file
        image = Image.new('RGB', (64, 64), color='red')

    # Tạo menu với mô tả cách sử dụng
    menu = pystray.Menu(
        pystray.MenuItem(
            "Cách sử dụng Bộ Gõ AI:",
            None,
            enabled=False
        ),
        pystray.MenuItem(
            "- Double Space để scan",
            None,
            enabled=False
        ),
        pystray.MenuItem(
            "- Pause Break để scan",
            None,
            enabled=False
        ),
        pystray.MenuItem(
            "- Select text rồi Double Right Shift",
            None,
            enabled=False
        ),
        pystray.MenuItem(
            "- Select text rồi Pause Break/Double (Right) Shift",
            None,
            enabled=False
        ),
        pystray.MenuItem("Open Location", open_source_location),
        pystray.MenuItem("Restart Script", restart_script),
        pystray.MenuItem("Terminate Script", on_quit)
    )

    icon = pystray.Icon(
        "bo_go_ai",
        image,
        "Bộ Gõ AI (Double Space/Pause Break để scan)",
        menu
    )

    return icon

# Thêm biến global để lưu trữ icon
tray_icon = None

# Thiết lập listener cho bàn phím
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Vòng lặp chính
try:
    print("Script đang chạy...")

    # Khởi tạo và chạy system tray icon trong thread riêng
    tray_icon = create_tray_icon()
    tray_icon.run_detached()

    while True:
        time.sleep(0.5)
        if should_scan:
            # Lưu clipboard trước khi bắt đầu
            save_clipboard()

            try:
                line, has_selection = get_selected_text()
                if line.strip():
                    print("\n" + "="*50)
                    print(f"Văn bản gốc: '{line}'")
                    corrected_text = get_correction(line)
                    print(f"Văn bản đã sửa: '{corrected_text}'")
                    print("="*50)
                    replace_current_line(corrected_text, has_selection)
            finally:
                # Đảm bảo luôn restore clipboard sau khi hoàn thành hoặc có lỗi
                restore_clipboard()

            should_scan = False

except KeyboardInterrupt:
    is_calling_api = False
    listener.stop()
    if tray_icon:
        tray_icon.stop()
    print("\nĐã dừng script.")
except Exception as e:
    print(f"Lỗi không mong muốn: {str(e)}")
    if tray_icon:
        tray_icon.stop()
