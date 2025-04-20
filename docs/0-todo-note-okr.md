## OKR

khi hover vao icon o taskbar tray
thi hien len chu
'Bo Go AI (....)'

toi muon them thong tin ve Model dang duoc su dung

## Kế hoạch triển khai "Hiển thị model đang dùng trong hover text của Tray Icon"

### 1. Tổng quan

-   **Mục tiêu**: Hiển thị thông tin model OpenAI đang sử dụng (hiện tại là GPT-4o-mini) trong hover text của system tray icon
-   **Output dự kiến**: "Bộ Gõ AI (GPT-4o-mini)"

### 2. Files cần chỉnh sửa

1. **`src/ui/tray_icon.py`**: Đây là file chính cần chỉnh sửa để thay đổi hover text

    - Dòng 92-93: Phần khởi tạo icon với hover text

    ```python
    return pystray.Icon(
        "bo_go_ai",
        image,
        "Bộ Gõ AI (Double Right Shift/Backslash để auto-correct)",
        menu
    )
    ```

2. **`config/settings.py`**: File chứa cấu hình MODEL_NAME, cần import vào tray_icon.py
    - MODEL_NAME đã được định nghĩa (dòng 20): `MODEL_NAME = "gpt-4o-mini"`

### 3. Các bước triển khai

1. Trong file `src/ui/tray_icon.py`:
    - Import MODEL_NAME từ config.settings
    - Cập nhật hover text để bao gồm MODEL_NAME

### 4. Mã cần thêm/sửa

```python
# Trong src/ui/tray_icon.py
# Cập nhật import line để thêm MODEL_NAME
from config.settings import APP_NAME, ICON_PATH, RAG_CONTEXT_FOLDER, MODEL_NAME

# Cập nhật hover text trong phương thức create_menu()
return pystray.Icon(
    "bo_go_ai",
    image,
    f"{APP_NAME} ({MODEL_NAME})",
    menu
)
```

### 5. Lợi ích

-   User có thể nhìn vào hover text và biết ngay mô hình đang được sử dụng
-   Dễ dàng xác nhận khi đổi model (ví dụ: từ GPT-4o-mini sang GPT-4.1-mini)
-   Tối ưu debugging/testing và trải nghiệm developer
