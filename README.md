# Bộ Gõ AI Tiếng Việt / AI Vietnamese Typing Tool

Đây là một bộ gõ tiếng Việt thông minh tích hợp AI và RAG (Retrieval Augmented Generation) cho Windows 10, được viết bằng Python. Ứng dụng có khả năng tự động sửa lỗi chính tả, định dạng văn bản và điều chỉnh ngữ cảnh theo thời gian thực, với khả năng tham chiếu thêm ngữ cảnh từ thư mục RAG để tăng độ chính xác. / This is an intelligent Vietnamese typing tool integrated with AI and RAG (Retrieval Augmented Generation) for Windows 10, written in Python. The application has the ability to automatically correct spelling errors, format text, and adjust context in real-time, with additional context referencing from RAG folder for enhanced accuracy.

## Tính năng chính / Key Features

-   **Sửa lỗi thông minh**: Tự động sửa lỗi chính tả, typo và định dạng văn bản với hai chế độ: cơ bản và nâng cao (với RAG context) / **Smart Correction**: Automatically corrects spelling errors, typos, and text formatting with two modes: basic and advanced (with RAG context).
-   **Hỗ trợ đa ngôn ngữ**: Tiếng Việt và tiếng Anh, với khả năng xử lý văn bản song ngữ / **Multilingual Support**: Vietnamese and English, with bilingual text processing capabilities.
-   **Tùy chỉnh ngữ cảnh**:
    - Cơ bản: Định nghĩa các quy tắc sửa lỗi trong my_prompt.md
    - Nâng cao: Thêm các file .md vào thư mục rag_context để mở rộng ngữ cảnh
    / **Context Customization**:
    - Basic: Define correction rules in my_prompt.md
    - Advanced: Add .md files to rag_context folder for extended context
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

2. Kích hoạt sửa lỗi bằng một trong ba cách: / Activate correction in one of three ways:

    - Nhấn đúp phím Space (cách) / Double press the Space key
    - Nhấn đúp phím Shift phải / Double press the Right Shift key
    - Nhấn phím Scroll Lock / Press the Scroll Lock key

3. Tùy chỉnh ngữ cảnh: / Customize context:
    - Chỉnh sửa file `my_prompt.md` để thêm các quy tắc riêng / Edit the `my_prompt.md` file to add your own rules
    - Ví dụ: thay thế "mr." thành "Mr.", "thầy" thành "Thầy" / For example: replace "mr." with "Mr.", "thầy" with "Thầy"


# Hướng dẫn tự động chạy script Python khi khởi động Windows

## Tạo shortcut trong thư mục Startup

1. **Tạo file .bat để chạy script Python:**

   Tạo file `run_bo_go_ai.bat` với nội dung sau:

   ```bash
   @echo off
   cd /d "%~dp0"
   pythonw "run_main.py"
   ```

2. **Mở thư mục Startup bằng cách:**
   - Nhấn `Windows + R`
   - Gõ `shell:startup`
   - Nhấn `Enter`

3. **Copy shortcut của file .bat vào thư mục Startup**

© 2024 IRONTAN Vietnam LTD. Bản quyền thuộc về IRONTAN Vietnam LTD. Theo giấy phép GNU. / © 2024 IRONTAN Vietnam LTD. All rights reserved by IRONTAN Vietnam LTD. Under the GNU license.
