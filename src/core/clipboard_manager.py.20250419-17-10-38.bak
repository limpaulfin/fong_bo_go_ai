"""
Module quản lý clipboard, hỗ trợ việc lưu trữ và khôi phục nội dung clipboard.
"""
import pyperclip
import time
from pynput.keyboard import Key, Controller

class ClipboardManager:
    def __init__(self):
        self.keyboard = Controller()
        self.original_content = None

    def save_state(self):
        """Lưu trạng thái clipboard hiện tại"""
        try:
            self.original_content = pyperclip.paste()
        except Exception as e:
            print(f"Lỗi khi lưu clipboard: {str(e)}")
            self.original_content = ''

    def restore_state(self):
        """Khôi phục trạng thái clipboard đã lưu"""
        if self.original_content is not None:
            max_retries = 3
            for _ in range(max_retries):
                try:
                    pyperclip.copy(self.original_content)
                    if pyperclip.paste() == self.original_content:
                        break
                except Exception as e:
                    print(f"Lỗi khi khôi phục clipboard: {str(e)}")
                time.sleep(0.1)

    def get_selected_text(self, trigger_source):
        """Lấy văn bản được chọn hoặc văn bản từ vị trí hiện tại đến đầu dòng"""
        self.save_state()
        has_selection = False
        selected_text = ""

        try:
            # Thử lấy selection hiện tại (nếu có)
            with self.keyboard.pressed(Key.ctrl):
                self.keyboard.tap('c')
            time.sleep(0.1)

            selected_text = pyperclip.paste()
            has_selection = selected_text != self.original_content and selected_text.strip() != ""

            # Xử lý xóa ký tự khi sử dụng double backslash hoặc double right shift
            if trigger_source == 'double_backslash' and not has_selection:
                # Xóa 2 dấu backslash
                self.keyboard.press(Key.backspace)
                self.keyboard.release(Key.backspace)
                time.sleep(0.01)
                self.keyboard.press(Key.backspace)
                self.keyboard.release(Key.backspace)
                time.sleep(0.01)

            # Cả double_right_shift và double_backslash đều xử lý giống nhau sau bước xóa ký tự

            if not has_selection:
                # Select từ vị trí hiện tại đến đầu dòng
                self.keyboard.press(Key.shift)
                self.keyboard.press(Key.home)
                self.keyboard.release(Key.home)
                self.keyboard.release(Key.shift)
                time.sleep(0.1)

                # Copy với retry
                max_retries = 3
                for _ in range(max_retries):
                    with self.keyboard.pressed(Key.ctrl):
                        self.keyboard.tap('c')
                    time.sleep(0.1)

                    selected_text = pyperclip.paste()
                    if selected_text and selected_text != self.original_content:
                        break
                    time.sleep(0.1)

                # Nếu vẫn không lấy được text, return luôn
                if not selected_text or selected_text == self.original_content:
                    return "", False

                # Hủy selection
                self.keyboard.tap(Key.right)

            return selected_text, has_selection

        except Exception as e:
            print(f"Lỗi khi lấy text: {str(e)}")
            return "", False

        finally:
            # Đảm bảo luôn restore clipboard sau 1 khoảng thời gian
            time.sleep(0.1)
            self.restore_state()

    def replace_current_line(self, new_text, has_selection):
        """Thay thế dòng hiện tại bằng text mới"""
        self.save_state()
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
                with self.keyboard.pressed(Key.ctrl):
                    self.keyboard.tap('v')
                time.sleep(0.1)
            else:
                # Select từ vị trí hiện tại đến đầu dòng
                self.keyboard.press(Key.shift)
                self.keyboard.press(Key.home)
                self.keyboard.release(Key.home)
                self.keyboard.release(Key.shift)
                time.sleep(0.1)

                # Paste text mới
                with self.keyboard.pressed(Key.ctrl):
                    self.keyboard.tap('v')
                time.sleep(0.1)

                # Di chuyển con trỏ về cuối
                self.keyboard.tap(Key.end)

        finally:
            # Restore clipboard gốc
            time.sleep(0.2)
            self.restore_state()
