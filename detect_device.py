# check xem may nay co phai may Lenovo khong?
import platform

def is_lenovo():
    # Lấy thông tin về hệ thống
    system_info = platform.uname()

    # Kiểm tra tên máy
    if "LENOVO" in system_info.node.upper():
        return True
    return False

# Kiểm tra và in kết quả
if is_lenovo():
    print("Máy hiện tại là máy LENOVO.")
else:
    print("Máy hiện tại không phải là máy LENOVO.")
