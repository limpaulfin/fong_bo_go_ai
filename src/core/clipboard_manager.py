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
            # Code xử lý get_selected_text từ file gốc
            # ...
            return selected_text, has_selection
        except Exception as e:
            print(f"Lỗi khi lấy text: {str(e)}")
            return "", False
        finally:
            self.restore_state()
