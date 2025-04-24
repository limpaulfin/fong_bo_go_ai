## OKR

### 5. Lợi ích

---

## OKR 2: Mở rộng Trigger sang Double Left/Right Shift

-   **Mục tiêu**: Cho phép kích hoạt auto-correct bằng cách nhấn đúp phím `Left Shift` hoặc `Right Shift` (thay vì chỉ `Right Shift` như hiện tại).
-   **Lý do**: Tăng tính linh hoạt cho người dùng, phù hợp với thói quen sử dụng phím `Shift` khác nhau.
-   **Files cần chỉnh sửa**: `src/core/keyboard_handler.py` (dự kiến)
-   **Các bước dự kiến**:
    1. Xác định logic xử lý `Double Right Shift`.
    2. Mở rộng logic để bao gồm cả `Left Shift`.
    3. Đảm bảo logic double-press hoạt động đúng cho cả hai phím.
    4. Kiểm tra lại.
-   **Trạng thái**: Đã hoàn thành (2025-04-24)

---

## OKR 3: Thêm Trigger Double Num Lock

-   **Mục tiêu**: Cho phép kích hoạt auto-correct bằng cách nhấn đúp phím `Num Lock`.
-   **Lý do**: Cung cấp thêm một tùy chọn trigger tiện lợi cho người dùng.
-   **Files cần chỉnh sửa**: `src/core/keyboard_handler.py`
-   **Các bước dự kiến**:
    1. Thêm biến trạng thái `last_num_lock_time`.
    2. Thêm khối `elif key == Key.num_lock:` vào `on_press`.
    3. Implement logic double-press cho `Num Lock`.
    4. Reset các timer khác khi cần thiết.
    5. Kiểm tra lại.
-   **Trạng thái**: Đã hoàn thành (2025-04-24)

---

## OKR 4: Cập nhật Tài liệu và UI

-   **Mục tiêu**: Phản ánh các trigger bàn phím mới (Double Shift, Double Num Lock) vào README.md và hover text của Tray Icon. **Đồng thời, cập nhật danh sách trigger trong menu của Tray Icon cho chính xác và gọn gàng.**
-   **Lý do**: Đảm bảo tài liệu và thông tin hiển thị cho người dùng là chính xác và cập nhật.
-   **Files cần chỉnh sửa**:
    -   `README.md`
    -   `src/ui/tray_icon.py`
-   **Các bước dự kiến**:
    1. Cập nhật phần "Cách sử dụng" trong `README.md`.
    2. Cập nhật hover text trong `src/ui/tray_icon.py`.
    3. **Cấu trúc lại các MenuItem mô tả trigger trong menu của `src/ui/tray_icon.py`.**
    4. Kiểm tra lại.
-   **Trạng thái**: Đã hoàn thành (2025-04-24)

---

## OKR 5: Hoàn nguyên Trigger Double Shift & Xác nhận Scroll Lock

-   **Mục tiêu**: Đưa logic trigger về chỉ chấp nhận `Double Right Shift`. Xác nhận `Scroll Lock` vẫn hoạt động và cập nhật tài liệu/UI tương ứng.
-   **Lý do**: Theo yêu cầu người dùng, điều chỉnh lại hành vi trigger.
-   **Files cần chỉnh sửa**:
    -   `src/core/keyboard_handler.py`
    -   `src/ui/tray_icon.py`
    -   `README.md`
-   **Các bước dự kiến**:
    1. Hoàn nguyên logic `Double Shift` trong `keyboard_handler.py`.
    2. Xác nhận `Scroll Lock` hoạt động trong `keyboard_handler.py`.
    3. Cập nhật mô tả `Double Shift` trong `tray_icon.py` (menu và hover text).
    4. Cập nhật mô tả `Double Shift` trong `README.md`.
    5. Kiểm tra lại.
-   **Trạng thái**: Đã hoàn thành (2025-04-24)
