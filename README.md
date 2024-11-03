# Bộ Gõ AI Tiếng Việt / AI Vietnamese Typing Tool

Đây là một bộ gõ tiếng Việt thông minh tích hợp AI cho Windows 10, được viết bằng Python. Ứng dụng có khả năng tự động sửa lỗi chính tả, định dạng văn bản và điều chỉnh ngữ cảnh theo thời gian thực. / This is an intelligent Vietnamese typing tool integrated with AI for Windows 10, written in Python. The application has the ability to automatically correct spelling errors, format text, and adjust context in real-time.

## Tính năng chính / Key Features

-   **Sửa lỗi thông minh**: Tự động sửa lỗi chính tả, typo và định dạng văn bản / **Smart Correction**: Automatically corrects spelling errors, typos, and text formatting.
-   **Hỗ trợ đa ngôn ngữ**: Tiếng Việt và tiếng Anh / **Multilingual Support**: Vietnamese and English.
-   **Tùy chỉnh ngữ cảnh**: Cho phép định nghĩa các quy tắc sửa lỗi riêng / **Context Customization**: Allows defining custom correction rules.
-   **Theo dõi thống kê**: Thống kê số lượng token sử dụng theo ngày/tháng / **Statistics Tracking**: Tracks the number of tokens used daily/monthly.
-   **Ghi log**: Lưu lại lịch sử các thay đổi để tham khảo sau này / **Logging**: Saves the history of changes for future reference.

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
