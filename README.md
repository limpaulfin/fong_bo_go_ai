# Bộ Gõ AI Tiếng Việt / AI Vietnamese Typing Tool

## Release Notes

### v1.4 (2024-03-11)
- **Cải tiến phím tắt**:
  - Thêm tính năng RAG context khi chọn văn bản + Scroll Lock
  - Tối ưu hóa xử lý phím tắt để tránh xung đột
- **Cải thiện giao diện System Tray**:
  - Thêm nút mở nhanh README.md
  - Cập nhật hướng dẫn sử dụng rõ ràng hơn
  - Phân loại chức năng theo có/không có RAG context
- **Tối ưu hóa xử lý RAG context**:
  - Cải thiện độ chính xác khi sử dụng ngữ cảnh bổ sung
  - Thêm khả năng tự động nhận diện và giải thích thuật ngữ chuyên ngành

## Giới thiệu / Introduction

Đây là một bộ gõ tiếng Việt thông minh tích hợp AI và RAG (Retrieval Augmented Generation) cho Windows 10, được viết bằng Python. Ứng dụng có khả năng tự động sửa lỗi chính tả, định dạng văn bản và điều chỉnh ngữ cảnh theo thời gian thực, với khả năng tham chiếu thêm ngữ cảnh từ thư mục RAG để tăng độ chính xác. / This is an intelligent Vietnamese typing tool integrated with AI and RAG (Retrieval Augmented Generation) for Windows 10, written in Python. The application has the ability to automatically correct spelling errors, format text, and adjust context in real-time, with additional context referencing from RAG folder for enhanced accuracy.

## Tính năng chính / Key Features

-   **Sửa lỗi thông minh**: Tự động sửa lỗi chính tả, typo và định dạng văn bản với hai chế độ: cơ bản và nâng cao (với RAG context) / **Smart Correction**: Automatically corrects spelling errors, typos, and text formatting with two modes: basic and advanced (with RAG context).
-   **Hỗ trợ đa ngôn ngữ**: Tiếng Việt và tiếng Anh, với khả năng xử lý văn bản song ngữ / **Multilingual Support**: Vietnamese and English, with bilingual text processing capabilities.
-   **Tùy chỉnh ngữ cảnh**:
    - Cơ bản: Định nghĩa các quy tắc sửa lỗi trong my_prompt.md
    - Nâng cao: Thêm các file .md vào thư mục rag_context để mở rộng ngữ cảnh
-   **Theo dõi thống kê**: Thống kê chi tiết số lượng token sử dụng theo ngày/tháng, phân biệt theo loại trigger / **Statistics Tracking**: Detailed token usage statistics by day/month, differentiated by trigger type.
-   **Ghi log**: Lưu lại lịch sử các thay đổi và API responses để tham khảo và debug / **Logging**: Saves history of changes and API responses for reference and debugging.
-   **System Tray Integration**: Truy cập nhanh các tính năng và hướng dẫn sử dụng qua system tray icon / **System Tray Integration**: Quick access to features and usage guide via system tray icon.

## Cài đặt / Installation

1. Cài đặt Python 3.x từ [python.org](https://www.python.org/) / Install Python 3.x from [python.org](https://www.python.org/)

2. Clone repository này về máy: / Clone this repository to your machine:

    ```bash
    git clone https://github.com/limpaulfin/fong_bo_go_ai
    ```

3. Cài đặt các thư viện cần thiết: / Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

4. Tạo file `.env` và thêm API key OpenAI: / Create a `.env` file and add your OpenAI API key:
    ```
    OPENAI_API_KEY=your_api_key_here
    ```

## Cách sử dụng / How to Use

1. Chạy ứng dụng: / Run the application:

    ```bash
    python run_main.py
    ```

2. Các phím tắt chính: / Main shortcuts:

    **Chế độ cơ bản (không có RAG context)**: / Basic mode (without RAG context):
    - Nhấn đúp phím Space (cách) / Double press the Space key
    - Nhấn đúp phím Shift phải / Double press the Right Shift key
    - Nhấn phím Scroll Lock (không chọn text) / Press Scroll Lock (without text selection)

    **Chế độ nâng cao (có RAG context)**: / Advanced mode (with RAG context):
    - Nhấn đúp phím Backslash (\\) / Double press the Backslash key
    - Chọn văn bản + Nhấn Scroll Lock / Select text + Press Scroll Lock

3. Tùy chỉnh ngữ cảnh: / Customize context:
    - Chỉnh sửa file `my_prompt.md` để thêm các quy tắc riêng / Edit `my_prompt.md` to add custom rules
    - Thêm file .md vào thư mục `rag_context` để mở rộng ngữ cảnh / Add .md files to `rag_context` folder for extended context

4. Truy cập nhanh qua System Tray: / Quick access via System Tray:
    - Xem hướng dẫn sử dụng / View usage guide
    - Mở file README.md / Open README.md
    - Mở thư mục mã nguồn / Open source location
    - Mở thư mục RAG context / Open RAG context folder
    - Khởi động lại ứng dụng / Restart application
    - Thoát ứng dụng / Exit application

© 2024 IRONTAN Vietnam LTD. Bản quyền thuộc về IRONTAN Vietnam LTD. Theo giấy phép GNU. / © 2024 IRONTAN Vietnam LTD. All rights reserved by IRONTAN Vietnam LTD. Under the GNU license.
