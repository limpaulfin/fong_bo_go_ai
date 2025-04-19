import os
import pystray
from PIL import Image

class SystemTrayIcon:
    def __init__(self, on_quit_callback):
        self.on_quit_callback = on_quit_callback
        self.icon = None

    def create_menu(self):
        def on_quit(icon):
            """Xử lý thoát script"""
            icon.stop()
            self.on_quit_callback()

        def restart_script(icon):
            """Khởi động lại script"""
            icon.stop()
            script_path = os.path.abspath(__file__)
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(script_path)))
            if os.name == 'nt':  # Windows
                os.system(f'start pythonw "{os.path.join(base_dir, "main.py")}"')
            else:  # Linux/Mac
                os.system(f'python3 "{os.path.join(base_dir, "main.py")}" &')
            os._exit(0)

        def open_source_location(icon):
            """Mở thư mục chứa file mã nguồn"""
            script_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            os.startfile(script_dir) if os.name == 'nt' else os.system(f'xdg-open "{script_dir}"')

        def open_rag_folder(icon):
            """Mở thư mục RAG context"""
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            rag_dir = os.path.join(base_dir, "rag_context")
            if not os.path.exists(rag_dir):
                os.makedirs(rag_dir)
            os.startfile(rag_dir) if os.name == 'nt' else os.system(f'xdg-open "{rag_dir}"')

        def open_readme(icon):
            """Mở file README.md"""
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            readme_path = os.path.join(base_dir, "README.md")
            os.startfile(readme_path) if os.name == 'nt' else os.system(f'xdg-open "{readme_path}"')

        # Load icon image từ thư mục gốc của project
        try:
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            icon_path = os.path.join(base_dir, "icon.png")
            image = Image.open(icon_path)
        except Exception as e:
            print(f"Lỗi khi load icon từ {icon_path}: {str(e)}")
            # Tạo icon mặc định nếu không load được file
            image = Image.new('RGB', (64, 64), color='red')

        # Tạo menu với mô tả cách sử dụng
        menu = pystray.Menu(
            pystray.MenuItem(
                "Cách sử dụng Bộ Gõ AI:",
                None,
                enabled=False
            ),
            pystray.MenuItem(
                "- Double Right Shift: Auto-correct (có RAG) - mọi thiết bị",
                None,
                enabled=False
            ),
            pystray.MenuItem(
                "- Chọn văn bản + Double Right Shift: Auto-correct (có RAG)",
                None,
                enabled=False
            ),
            pystray.MenuItem(
                "- Double Backslash (\\): Auto-correct (có RAG)",
                None,
                enabled=False
            ),
            pystray.MenuItem(
                "- Chọn văn bản + Scroll Lock: Auto-correct (có RAG)",
                None,
                enabled=False
            ),
            pystray.MenuItem("Open README.md", open_readme),
            pystray.MenuItem("Open Location", open_source_location),
            pystray.MenuItem("Open RAG folder (context)", open_rag_folder),
            pystray.MenuItem("Restart Script", restart_script),
            pystray.MenuItem("Terminate Script", on_quit)
        )

        return pystray.Icon(
            "bo_go_ai",
            image,
            "Bộ Gõ AI (Double Right Shift/Backslash để auto-correct)",
            menu
        )

    def run_detached(self):
        self.icon = self.create_menu()
        self.icon.run_detached()

    def stop(self):
        if self.icon:
            self.icon.stop()
