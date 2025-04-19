# OKR

## Nhiệm vụ hiện tại

1. Thống nhất chức năng double backslash (\\) và double right shift

    - Cả hai phím tắt đều sẽ luôn sử dụng RAG context (điều kiện này đã được cập nhật)
    - Xử lý xóa dấu backslash khi sử dụng double backslash cần được thống nhất với double right shift:
        - Kiểm tra và sửa phần `get_selected_text()` để xử lý giống nhau giữa 2 phím tắt
        - Kiểm tra các hàm `show_api_status()` và `clear_api_status()` đảm bảo chúng hoạt động chính xác với cả 2 phím tắt
        - Đảm bảo indicator "::." hiển thị và xử lý giống nhau cho cả 2 phím tắt

2. Cập nhật tài liệu hướng dẫn sử dụng
    - Cập nhật docs/huong_dan_su_dung.md để phản ánh cả hai phím tắt đều sử dụng RAG context
    - Cập nhật menu trong system tray (cả trong run_main.py và src/ui/tray_icon.py)
    - Thống nhất mô tả chức năng trong các phần mô tả khác của ứng dụng

## Nhiệm vụ đã hoàn thành

✅ Thay đổi indicator khi gọi API từ dấu `...` thành `::..` (2 dấu hai chấm, và 2 dấu chấm)

-   Đã sửa code trong hàm hiển thị trạng thái API
-   Đã cập nhật cả phần hiển thị và xóa indicator
-   Đã áp dụng cho tất cả trường hợp gọi API
-   File đã cập nhật: run_main.py
-   Ngày hoàn thành: 2025-04-19

✅ nhấn double shift thì kích hoạt được chức năng auto correct

-   Đã sửa tính năng Double Right Shift để áp dụng cho tất cả thiết bị (đã xóa điều kiện is_lenovo)
-   File đã cập nhật: src/core/keyboard_handler.py và run_main.py
-   Ngày hoàn thành: 2025-04-19

## Nhiệm vụ tiếp theo

-   Kiểm tra và đảm bảo tính năng hoạt động trên tất cả các thiết bị
-   Cập nhật tài liệu hướng dẫn sử dụng nếu cần
