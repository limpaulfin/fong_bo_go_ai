import os
import pystray
from PIL import Image

class SystemTrayIcon:
    def __init__(self, on_quit_callback):
        self.on_quit_callback = on_quit_callback
        self.icon = None

    def create_menu(self):
        # Code từ hàm create_tray_icon() trong file gốc
        pass

    def run_detached(self):
        self.icon = self.create_menu()
        self.icon.run_detached()

    def stop(self):
        if self.icon:
            self.icon.stop()
