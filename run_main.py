"""
Bộ gõ Auto Correct bằng AI - Công cụ hỗ trợ gõ và auto correct văn bản thông minh với AI và RAG technique.

Chức năng chính:
- Theo dõi và sửa lỗi văn bản real-time (real-time text correction)
- Hỗ trợ đa ngôn ngữ: Tiếng Việt, Tiếng Anh (multilingual support)
- Tự động thống kê token usage (token usage tracking)
- Xử lý thông minh với context và RAG context (context-aware processing)

Cách kích hoạt:
1. Double Space: Auto-correct cơ bản (không có RAG context) ← disabled (vi cam thay kho chiu)
2. Double Backslash (\\): Auto-correct với RAG context từ thư mục rag_context
3. Double Right Shift: Auto-correct cho text đã chọn (không có RAG context) ← cung disabled (vi cam thay kho chiu)
4. Scroll Lock: Tương tự Double Space

Cách hoạt động:
1. Theo dõi keyboard input (keyboard monitoring)
2. Khi phát hiện trigger (double space/backslash/right shift/scroll lock):
   - Nếu có text được chọn: sử dụng text đó
   - Nếu không: lấy text từ vị trí con trỏ đến đầu dòng
3. Xử lý văn bản:
   - Double Space/Right Shift/Scroll Lock: sửa lỗi cơ bản
   - Double Backslash: sửa lỗi với RAG context để xử lý chính xác hơn
4. Thay thế văn bản cũ bằng văn bản đã sửa
5. Tự động thống kê và lưu log token usage

Tính năng bổ sung:
- System tray icon với menu hướng dẫn
- Quản lý clipboard thông minh
- Theo dõi token usage theo ngày/tháng
- Log API responses để debug
- RAG context folder để lưu trữ ngữ cảnh bổ sung

Author: [Fong - IRONTAN Vietnam Limited]
Version: 1.0.0
Last updated: 2025-04-19
"""

import os
import time
import sys
from detect_device import is_lenovo
from dotenv import load_dotenv
from config.settings import LOG_FOLDER, RAG_CONTEXT_FOLDER

# Import các module đã tạo
from src.core.keyboard_handler import KeyboardHandler
from src.core.clipboard_manager import ClipboardManager
from src.text_processor.api_handler import get_correction
from src.ui.tray_icon import SystemTrayIcon
from src.utils.debug_logger import log_selected_text, log_correction

# Tạo thư mục logs và rag_context nếu chưa tồn tại
os.makedirs(LOG_FOLDER, exist_ok=True)
os.makedirs(RAG_CONTEXT_FOLDER, exist_ok=True)

# Load environment variables
load_dotenv()

# Khởi tạo các thành phần
keyboard_handler = KeyboardHandler()
clipboard_manager = ClipboardManager()
should_scan = False

# Thiết lập trạng thái Lenovo
keyboard_handler.set_lenovo_status(is_lenovo())

def on_quit():
    """Xử lý khi thoát ứng dụng"""
    keyboard_handler.stop_listening()
    print("\nĐã dừng script.")
    sys.exit(0)

def main():
    """Hàm chính của ứng dụng"""
    global should_scan

    try:
        print("Script đang chạy...")
        print("Chức năng: Double Right Shift để autocorrect text đã chọn")

        # Khởi tạo và chạy system tray icon trong thread riêng
        tray_icon = SystemTrayIcon(on_quit)
        tray_icon.run_detached()

        # Bắt đầu lắng nghe sự kiện bàn phím
        keyboard_handler.start_listening()

        # Vòng lặp chính
        while True:
            time.sleep(0.3)

            # Cập nhật trạng thái từ keyboard handler
            should_scan = keyboard_handler.should_scan

            if should_scan:
                keyboard_handler.should_scan = False  # Reset trạng thái

                try:
                    # Lấy text đã chọn hoặc dòng hiện tại
                    line, has_selection = clipboard_manager.get_selected_text(keyboard_handler.trigger_source)

                    if line.strip():
                        # Log selected text ra console
                        log_selected_text(line, keyboard_handler.trigger_source)

                        # Gọi API để sửa lỗi cho tất cả các trường hợp (bao gồm double right shift)
                        corrected_text = get_correction(line, keyboard_handler.trigger_source, has_selection)

                        # Log kết quả correction
                        log_correction(line, corrected_text, keyboard_handler.trigger_source)

                        # Thay thế văn bản gốc bằng văn bản đã sửa
                        clipboard_manager.replace_current_line(corrected_text, has_selection)
                except Exception as e:
                    print(f"Lỗi khi xử lý văn bản: {str(e)}")

    except KeyboardInterrupt:
        on_quit()
    except Exception as e:
        print(f"Lỗi không mong muốn: {str(e)}")
        if 'tray_icon' in locals():
            tray_icon.stop()

if __name__ == "__main__":
    main()
