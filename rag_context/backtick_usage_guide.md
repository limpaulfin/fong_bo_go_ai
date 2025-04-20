# Quy tắc sử dụng backtick trong văn bản

## Tên file đơn giản

Với tên file đơn giản, sử dụng một cặp backtick:
`backtick_usage_guide.md`

## Đường dẫn file

Với đường dẫn file, cũng sử dụng một cặp backtick:
`C:\Users\HP\OneDrive\project-development\python_bo_go_ai\rag_context\backtick_usage_guide.md`

## Đoạn mã (code block)

Với đoạn mã nhiều dòng, sử dụng ba backtick mở và đóng, có thể kèm ngôn ngữ:

```python
self.keyboard.press(Key.shift)
self.keyboard.press(Key.home)
self.keyboard.release(Key.home)
self.keyboard.release(Key.shift)
time.sleep(0.1)
```

## Mã nội tuyến (inline code)

Với mã ngắn nằm trong văn bản, sử dụng một cặp backtick:
Ví dụ: Hàm `print()` dùng để hiển thị nội dung ra console.

## Chủ động nhận diện nội dung cần đặt trong backtick

Hãy chủ động nhận diện và sử dụng backtick cho các loại nội dung sau:

1. **Tên biến, hàm, lớp trong code**: `variable_name`, `function_name()`, `ClassName`
2. **Lệnh terminal/command line**: `cd /path/to/folder`, `git commit -m "message"`
3. **Phím tắt và tổ hợp phím**: `Ctrl+C`, `Alt+Tab`, `Double Right Shift`
4. **Tên file và đường dẫn**: `config.json`, `/etc/hosts`, `C:\Windows\System32`
5. **Cấu trúc dữ liệu và đoạn JSON/XML ngắn**: `{"key": "value"}`, `<tag>content</tag>`
6. **Giá trị cấu hình**: `true`, `false`, `null`, `0.5`, `"setting"`
7. **Phần mở rộng file**: `.md`, `.py`, `.json`
8. **Tên API endpoint**: `/api/v1/users`, `GET /orders`
9. **Tham số URL và query string**: `?page=1&limit=10`
10. **Biến môi trường**: `OPENAI_API_KEY`, `PATH`, `HOME`

Với đoạn mã dài hoặc có định dạng phức tạp, luôn sử dụng code block (```), và thêm tên ngôn ngữ nếu có thể để được syntax highlighting, ví dụ:

```python
def example_function():
    print("This is a code block with syntax highlighting")
```
