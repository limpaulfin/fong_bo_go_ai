from src.core.keyboard_handler import KeyboardHandler
from src.core.clipboard_manager import ClipboardManager
from src.utils.token_tracker import TokenUsageTracker
from src.utils.logger import APILogger
from src.ui.tray_icon import SystemTrayIcon
from detect_device import is_lenovo
import time
import os

def main():
    # Khởi tạo các components
    keyboard_handler = KeyboardHandler()
    clipboard_manager = ClipboardManager()
    token_tracker = TokenUsageTracker()
    api_logger = APILogger()

    # Thiết lập Lenovo status
    keyboard_handler.set_lenovo_status(is_lenovo())

    # Khởi tạo system tray
    def on_quit():
        keyboard_handler.stop_listening()
        os._exit(0)

    tray_icon = SystemTrayIcon(on_quit)

    try:
        print("Script đang chạy...")

        # Bắt đầu listening keyboard
        keyboard_handler.start_listening()

        # Chạy system tray
        tray_icon.run_detached()

        # Main loop
        while True:
            time.sleep(0.3)
            if keyboard_handler.should_scan:
                # Xử lý text correction
                # ...
                keyboard_handler.should_scan = False

    except KeyboardInterrupt:
        keyboard_handler.stop_listening()
        tray_icon.stop()
        print("\nĐã dừng script.")
    except Exception as e:
        print(f"Lỗi không mong muốn: {str(e)}")
        tray_icon.stop()

if __name__ == "__main__":
    main()
