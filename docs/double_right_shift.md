# Tính năng Double Right Shift

## Tổng quan

Tính năng Double Right Shift cho phép người dùng kích hoạt chức năng auto-correct bằng cách nhấn nhanh phím Right Shift hai lần liên tiếp. Tính năng này hoạt động trên tất cả các loại thiết bị, không chỉ giới hạn ở máy Lenovo.

## Cách hoạt động

1. Người dùng nhấn phím Right Shift hai lần nhanh trong khoảng thời gian ngắn (mặc định: 0.2 giây)
2. Hệ thống nhận diện hành động này và kích hoạt chức năng auto-correct
3. Dữ liệu văn bản được gửi đến API để xử lý
4. Văn bản được sửa sẽ thay thế văn bản gốc

## Chi tiết kỹ thuật

### Cấu trúc mã nguồn

Tính năng này được triển khai trong `src/core/keyboard_handler.py`:

```python
def on_press(self, key):
    try:
        # Xử lý Double Right Shift - áp dụng cho tất cả thiết bị
        if key == Key.shift_r:
            current_time = time.time()
            time_diff = current_time - self.last_right_shift_time

            if time_diff < DOUBLE_SPACE_THRESHOLD:
                self.should_scan = True
                self.trigger_source = 'double_right_shift'

            self.last_right_shift_time = current_time

        # ... phần code khác ...
```

### Các thành phần chính

1. **Phát hiện phím nhấn**: Sử dụng thư viện pynput để theo dõi sự kiện bàn phím
2. **Đo thời gian giữa các lần nhấn**: Sử dụng `time.time()` để tính khoảng cách giữa hai lần nhấn Right Shift
3. **Kích hoạt**: Đặt `should_scan = True` khi phát hiện hai lần nhấn liên tiếp
4. **Xác định nguồn kích hoạt**: Đặt `trigger_source = 'double_right_shift'` để phân biệt với các phương pháp kích hoạt khác

### Cấu hình

Thời gian giữa hai lần nhấn được cấu hình trong `config/settings.py`:

```python
DOUBLE_SPACE_THRESHOLD = 0.2  # Thời gian tối đa giữa 2 lần nhấn (giây)
```

## Ưu điểm

1. **Dễ sử dụng**: Người dùng không cần nhớ tổ hợp phím phức tạp
2. **Không xung đột**: Ít xung đột với các phím tắt của ứng dụng khác
3. **Tương thích tốt**: Hoạt động trên mọi bàn phím với phím Right Shift

## Lưu ý

- Một số bàn phím có thể có độ nhạy khác nhau, ảnh hưởng đến khả năng nhận diện
- Người dùng có thể cần điều chỉnh giá trị `DOUBLE_SPACE_THRESHOLD` để phù hợp với tốc độ gõ của họ
