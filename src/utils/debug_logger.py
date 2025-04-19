"""
Module hỗ trợ debug và logging đơn giản, tập trung vào in thông tin ra console
"""

def log_selected_text(text, source):
    """
    Ghi log văn bản đã chọn ra console

    Args:
        text (str): Văn bản đã chọn
        source (str): Nguồn kích hoạt (ví dụ: 'double_right_shift')
    """
    border = "="*50
    print(f"\n{border}")
    print(f"TRIGGER: {source}")
    print(f"SELECTED TEXT: '{text}'")
    print(f"{border}")

def log_correction(original_text, corrected_text, source):
    """
    Ghi log kết quả autocorrect ra console

    Args:
        original_text (str): Văn bản gốc
        corrected_text (str): Văn bản đã sửa
        source (str): Nguồn kích hoạt (ví dụ: 'double_right_shift')
    """
    border = "-"*50
    print(f"\n{border}")
    print(f"SOURCE: {source}")
    print(f"ORIGINAL: '{original_text}'")
    print(f"CORRECTED: '{corrected_text}'")

    # Hiển thị số ký tự trước và sau
    print(f"ORIGINAL LENGTH: {len(original_text)} characters")
    print(f"CORRECTED LENGTH: {len(corrected_text)} characters")

    # Phát hiện sự khác biệt
    if original_text != corrected_text:
        print(f"STATUS: Text đã được thay đổi")
    else:
        print(f"STATUS: Không có thay đổi")
    print(f"{border}\n")
