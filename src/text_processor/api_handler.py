"""
Module xử lý các cuộc gọi đến OpenAI API và xử lý kết quả
"""
import json
import re
from openai import OpenAI
from config.settings import OPENAI_API_KEY, TEMPERATURE
from src.utils.logger import APILogger
from src.utils.token_tracker import TokenUsageTracker
from src.text_processor.context_handler import read_context, read_rag_context, get_no_rag_context
from pynput.keyboard import Key, Controller

keyboard_controller = Controller()
is_calling_api = False
api_logger = APILogger()
token_tracker = TokenUsageTracker()
client = OpenAI(api_key=OPENAI_API_KEY)

def show_api_status():
    """
    Hiển thị trạng thái đang gọi API bằng cách thêm '::..'
    """
    global is_calling_api
    if is_calling_api:
        keyboard_controller.type('::..')

def clear_api_status():
    """
    Xóa trạng thái API bằng cách xóa indicator '::..''
    """
    for _ in range(4):
        keyboard_controller.press(Key.backspace)
        keyboard_controller.release(Key.backspace)
        import time
        time.sleep(0.01)

def get_correction(text, trigger_source, has_selection):
    """
    Gửi văn bản đến OpenAI API để sửa lỗi

    Args:
        text (str): Văn bản cần sửa
        trigger_source (str): Nguồn kích hoạt (double_backslash, double_right_shift, scroll_lock)
        has_selection (bool): Có selection hay không

    Returns:
        str: Văn bản đã được sửa
    """
    global is_calling_api
    print(f"Trigger source: {trigger_source}")

    try:
        is_calling_api = True
        show_api_status()

        # Đọc context từ file
        context = read_context()

        # Cập nhật điều kiện để cả double_backslash và double_right_shift đều sử dụng RAG
        use_rag = trigger_source == 'double_backslash' or trigger_source == 'double_right_shift' or (trigger_source == 'scroll_lock' and has_selection)

        # Nếu bất kì trigger nào sử dụng RAG, thì dùng RAG context
        rag_context = read_rag_context() if use_rag else get_no_rag_context()

        # Tạo prompt
        prompt = f"""

        {context}

        {rag_context}

        ## Format:
        - json, nằm trong dấu ```json
        - cấu trúc của json trả về phải có cấu trúc như sau (đây chỉ là ví dụ):
            {{
                \"correction\": \"[văn bản được sửa]\"
            }}

        ## Input: \"\"\" {text} \"\"\"

        """

        print(f"Prompt: {prompt}")

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
        clear_api_status()

        # Debug: In ra response từ API để kiểm tra
        response = completion.choices[0].message.content.strip()
        print("Response after strip:", response)

        # Xử lý JSON response
        try:
            # Loại b các ký tự markdown ```json và ```
            json_text = re.sub(r'^```json\s*|\s*```$', '', response.strip())
            # Parse JSON
            result = json.loads(json_text)
            corrected_text = result.get("correction", text)

            # Log API response và cập nhật token usage
            api_logger.log_response(completion, text, corrected_text)
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
