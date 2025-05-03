# Quy tắc Hướng dẫn Biên tập Danh sách trong Văn bản

Tài liệu này cung cấp các quy tắc cần tuân thủ khi **biên tập thủ công** các danh sách (listing) trong văn bản nhập liệu để đảm bảo tính nhất quán và chuẩn mực. Người biên tập cần đọc hiểu ngữ cảnh để nhận diện ý định tạo danh sách và áp dụng định dạng phù hợp (danh sách gạch đầu dòng hoặc danh sách đánh số).

## 1. Định dạng Danh sách Gạch đầu dòng (`-`)

-   **Nhận diện:** Khi gặp một chuỗi các dòng ngắn liên tiếp mà ngữ cảnh cho thấy đó là một liệt kê (ví dụ: được giới thiệu bằng một câu/tiêu đề như "Bao gồm:", "Các điểm chính:", "Danh sách mua sắm:", hoặc đơn giản là các mục có vẻ cùng loại đứng liền nhau) nhưng **thiếu dấu `-`** ở đầu một hoặc nhiều mục.
-   **Thực hiện:** **Hãy thêm `- ` (dấu gạch ngang và một khoảng trắng) vào đầu mỗi dòng** thuộc về danh sách liệt kê đó để đảm bảo tính nhất quán.
-   **Mục đích:** Tạo và duy trì định dạng chuẩn cho danh sách liệt kê không cần thứ tự.

-   **Ví dụ 1 (Có dấu `:` giới thiệu):**
    _Nguyên bản:_

    ```
    Danh sách mua sắm:
    Sữa
    Trứng
    Bánh mì
    ```

    **Người biên tập cần sửa thành:**

    ```
    Danh sách mua sắm:
    - Sữa
    - Trứng
    - Bánh mì
    ```

-   **Ví dụ 2 (Không có dấu `:` giới thiệu):**
    _Nguyên bản:_

    ```
    Đặc điểm nổi bật
    Thiết kế đẹp
    Pin trâu
    Camera tốt
    ```

    **Người biên tập cần sửa thành:**

    ```
    Đặc điểm nổi bật:
    - Thiết kế đẹp
    - Pin trâu
    - Camera tốt
    ```

-   **Ví dụ 3 (Danh sách đã có nhưng thiếu mục):**
    _Nguyên bản:_

    ```
    Danh sách bạn bè:
    - Hương
    Đào
    Hồng

    Công việc cần làm:
    - Task 1
    ```

    **Người biên tập cần sửa thành:**

    ```
    Danh sách bạn bè:
    - Hương
    - Đào
    - Hồng

    Công việc cần làm:
    - Task 1
    ```

-   **Cảnh báo Quan trọng:** Quy tắc này hoạt động dựa trên ngữ cảnh và cấu trúc dòng. **KHÔNG ÁP DỤNG** quy tắc này cho các dòng nằm bên trong khối mã được đánh dấu bằng ba dấu backtick (```). Hãy kiểm tra kỹ ngữ cảnh trước khi thêm `- `.
    -   **Ví dụ lỗi cần tránh:**
        _Nguyên bản:_
        ```code
        Thuật ngữ kỹ thuật:
        DRY (Don't Repeat Yourself) principle
        RAG context structure
        ```
        **KHÔNG** được sửa thành:
        ```code
        Thuật ngữ kỹ thuật:
        - DRY (Don't Repeat Yourself) principle  <-- SAI
        - RAG context structure <-- SAI
        ```
        _Giữ nguyên mới là đúng._

## 2. Định dạng Danh sách Đánh số (`1.`, `2.`, ...)

-   **Nhận diện:** Khi gặp một chuỗi các dòng mà ngữ cảnh cho thấy đó là một quy trình, các bước, hoặc một liệt kê cần có thứ tự (ví dụ: được giới thiệu bằng một câu/tiêu đề như "Thực hiện theo các bước sau:", "Có 3 lý do:", "Kết quả là:") nhưng **thiếu số thứ tự, số không đúng, không liên tục, hoặc chưa viết hoa đúng chuẩn**.
-   **Thực hiện:**
    1.  **Thêm/Sửa số thứ tự:** Đảm bảo mỗi mục bắt đầu bằng số thứ tự đúng (`1.`, `2.`, `3.`, ...) và liên tục.
    2.  **Viết hoa đầu mục:** Đảm bảo chữ cái đầu tiên của nội dung sau số thứ tự được viết hoa.
    3.  **(Tùy chọn)** Viết hoa chữ cái đầu của câu giới thiệu nếu nó là một câu hoàn chỉnh đứng riêng.
-   **Mục đích:** Tạo và duy trì định dạng chuẩn, rõ ràng cho danh sách cần thể hiện thứ tự hoặc các bước.

-   **Ví dụ 1 (Thiếu số và chưa viết hoa):**
    _Nguyên bản:_

    ```
    Các bước thực hiện:
    1. chuẩn bị nguyên liệu
    2. sơ chế
    trộn đều
    4. nấu chín
    ```

    **Người biên tập cần sửa thành:**

    ```
    Các bước thực hiện:
    1. Chuẩn bị nguyên liệu
    2. Sơ chế
    3. Trộn đều
    4. Nấu chín
    ```

-   **Ví dụ 2 (Thiếu số, không liên tục, chưa viết hoa):**
    _Nguyên bản:_

    ```
    Danh sách thành viên:
    1. anh A
    chị B
    5. em C
    ```

    **Người biên tập cần sửa thành:**

    ```
    Danh sách thành viên:
    1. Anh A
    2. Chị B
    3. Em C
    ```

-   **Ví dụ 3 (Trường hợp đơn giản, thiếu số, chưa viết hoa):**
    _Nguyên bản:_
    ```
    nhà em có 3 người
    1. ba em
    2. mẹ em
    em
    ```
    **Người biên tập cần sửa thành:**
    ```
    Nhà em có 3 người
    1. Ba em
    2. Mẹ em
    3. Em
    ```
