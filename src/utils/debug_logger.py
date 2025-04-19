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
    print(f"{border}\n")
