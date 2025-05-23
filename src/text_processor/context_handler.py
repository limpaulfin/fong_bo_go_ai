"""
Module xử lý context và RAG context
"""
import os
import json
from config.settings import MY_PROMPT, RAG_CONTEXT_FOLDER

def read_context():
    """
    Đọc nội dung từ file my_prompt.md

    Returns:
        str: Nội dung của file context, hoặc chuỗi rỗng nếu có lỗi
    """
    try:
        if os.path.exists(MY_PROMPT):
            with open(MY_PROMPT, 'r', encoding='utf-8') as f:
                return f.read().strip()
        return ""
    except Exception as e:
        print(f"Lỗi khi đọc context: {str(e)}")
        return ""


def read_rag_context():
    """
    Scan và tìm file *.md và *.json (ngoại trừ file `README.md`) trong toàn bộ thư mục `rag_context` và trả về 1 chuỗi.
    Mỗi file sẽ cách nhau 1 dòng mới.
    """
    result = []
    directory = RAG_CONTEXT_FOLDER

    try:
        if not os.path.exists(directory):
            os.makedirs(directory)

        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            # Bỏ qua README.md và các thư mục
            if filename == 'README.md' or os.path.isdir(file_path):
                continue

            # Xử lý cả file .md và .json như file text thông thường
            if filename.endswith('.md') or filename.endswith('.json'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    if filename.endswith('.json'):
                        result.append(f"JSON từ file {filename}:\n{content}")
                    else:
                        result.append(content)

        rag_context = '\n\n'.join(result)
        return f"""

        ## QUYỀN VIẾT LẠI
        Nếu bạn cảm thấy nội dung chưa rõ nghĩa, hoặc bạn tin rằng bạn có thể viết lại hay hơn, chuẩn hơn, chính xác hơn, tốt hơn, bạn được phép làm như vậy. Hãy làm cho tốt nhé.

        ## EXTRA CONTEXT:
        - Tham khảo thêm ngữ cảnh (context) bổ sung sau đây để auto-correct cho chính xác.
        - ngữ cảnh bổ sung (extra context) có thể là danh sách các từ khóa, các thuật ngữ chuyên ngành, các thuật ngữ tiếng anh... hoặc các thông tin khác liên quan đến văn bản cần sửa.
        - ngữ cảnh bổ sung chỉ là để tham khảo, bạn hãy dựa trên kiến thức của bạn để đưa ra kết quả chính xác nhất, thậm chí mở rộng hơn nữa, hoặc cải tiến hơn nữa, hoặc sửa lại ngữ cảnh bổ sung để đảm bảo kết quả chính xác nhất.
        - kết quả trả về (OUTPUT), cần giải thích kèm theo trong dấu ngoặc đơn thuật ngữ chính xác (terminology) phía sau mỗi ý tiếng việt để đảm bảo rằng AI hiểu đúng điều tôi muốn truyền đạt.

        Ví dụ 1 : Hệ thống quản trị nội dung (CMS), công cụ tự động sửa lỗi (auto correct), hệ thống đăng ký (registration system), hệ thống báo lỗi (bug report system)...

        ví dụ 2:
        -- input: "đây là một ví dụ về cách sử dụng cong cụ sua loi"
        -- output: "Đây là một ví dụ về cách sử dụng công cụ tự động sửa lỗi (auto correct)."

        - nếu trong INPUT có các nội dung mang tính chất học thuật, khó hiểu, chuyên ngành mà bạn tin rằng người đọc sẽ không hiểu hoặc không biết hoặc sẽ nhầm lẫn, bạn cũng hay giải thích kèm theo trong dấu ngoặc đơn thuật ngữ chính xác (terminology) phía sau mỗi ý tiếng việt để đảm bảo rằng người đọc hiểu đúng điều tôi muốn truyền đạt. Các thuật ngữ này được lấy từ kiến thức của chính bạn, không phải trong ngữ cảnh bổ sung.


        ĐÂY LÀ YÊU CẦU BẮT BUỘC PHẢI ĐƯỢC THỰC HIỆN, KHÔNG ĐƯỢC BỎ QUA YÊU CẦU NÀY.

        Đây là ngữ cảnh bổ sung:
        \"\"\" {rag_context} \"\"\"
        """
    except Exception as e:
        print(f"Lỗi khi đọc file trong thư mục rag_context: {str(e)}")
        return ""


def get_no_rag_context():
    """
    Trả về context khi không sử dụng RAG
    """
    return """
    -   tôn trọng văn phong, không sửa đổi nội dung cốt lõi của INPUT
    -   tôn trọng ngữ pháp, ngữ điệu (nuance) của ngôn ngữ
    -   tôn trọng phong cách viết của tôi
    -   tôn trọng ngôn ngữ tiếng Việt hoặc tiếng Anh
    -   tôn trọng cách tôi xuống hàng. Nếu trong nội dung INPUT của tôi có xuống hàng, xin hãy đảm bảo trả về có xuống hàng (nếu điều đó là hợp lý)
    """


def log_context(text):
    """
    Ghi log context để training AI trong tương lai
    """
    try:
        with open(MY_PROMPT, "a", encoding="utf-8") as f:
            f.write(f"{text}\n")
    except Exception as e:
        print(f"Lỗi khi ghi context log: {str(e)}")
