# Hướng dẫn Sử dụng Fong Bo Go AI

## Giới thiệu

Fong Bo Go AI là công cụ hỗ trợ gõ và auto correct văn bản thông minh với AI và kỹ thuật RAG (Retrieval-Augmented Generation). Ứng dụng giúp tăng năng suất làm việc bằng cách tự động sửa lỗi và cải thiện văn bản trong thời gian thực.

## Cách kích hoạt

Ứng dụng hỗ trợ nhiều cách kích hoạt khác nhau:

1. **Nhấn 2 lần phím BackSlash (\\)**: Auto-correct với RAG context từ thư mục rag_context
2. **Nhấn 2 lần phím Right Shift**: Auto-correct cho text đã chọn (không có RAG context) - hoạt động trên tất cả thiết bị
3. **Nhấn phím Scroll Lock**: Auto-correct cơ bản (không có RAG context)
4. **Chọn văn bản + Nhấn Scroll Lock**: Auto-correct với RAG context

## Cách hoạt động

1. Ứng dụng theo dõi keyboard input trong nền
2. Khi phát hiện trigger (double backslash/right shift/scroll lock):
    - Nếu có text được chọn: sử dụng text đó
    - Nếu không: lấy text từ vị trí con trỏ đến đầu dòng
3. Xử lý văn bản:
    - Double Right Shift/Scroll Lock: sửa lỗi cơ bản
    - Double Backslash/Scroll Lock+Selection: sửa lỗi với RAG context để xử lý chính xác hơn
4. Thay thế văn bản cũ bằng văn bản đã sửa
5. Tự động thống kê và lưu log token usage

## Tính năng chính

-   **Sửa lỗi văn bản real-time**: Tự động nhận diện và sửa lỗi chính tả, ngữ pháp
-   **Hỗ trợ đa ngôn ngữ**: Tiếng Việt, Tiếng Anh
-   **Context-aware**: Xử lý thông minh với ngữ cảnh và RAG context
-   **System tray icon**: Quản lý ứng dụng dễ dàng qua menu tray
-   **Token tracking**: Theo dõi lượng token sử dụng theo ngày/tháng

## Thư mục RAG Context

Thư mục `rag_context` được sử dụng để lưu trữ các file .md chứa ngữ cảnh bổ sung. Khi kích hoạt với double backslash (\\\\), ứng dụng sẽ tham khảo các file này để đưa ra kết quả chính xác hơn.

## Các file quan trọng

-   **run_main.py**: File chính để khởi động ứng dụng
-   **my_prompt.md**: Chứa prompt mặc định cho AI
-   **config/settings.py**: Cấu hình ứng dụng
-   **src/core/keyboard_handler.py**: Xử lý sự kiện bàn phím
-   **.env**: Lưu khóa API (không được commit lên git)
