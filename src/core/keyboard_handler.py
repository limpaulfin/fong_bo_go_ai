"""
Module xử lý các sự kiện bàn phím, bao gồm phát hiện double right shift và các phím tắt khác.
"""
from pynput import keyboard
from pynput.keyboard import Key
import time
from config.settings import DOUBLE_SPACE_THRESHOLD

class KeyboardHandler:
    def __init__(self):
        self.should_scan = False
        self.last_space_time = 0
        self.space_count = 0
        self.last_backslash_time = 0
        self.last_right_shift_time = 0
        self.last_num_lock_time = 0
        self.trigger_source = None
        self.is_lenovo = False
        self.listener = None

    def set_lenovo_status(self, is_lenovo):
        """
        Thiết lập trạng thái thiết bị Lenovo
        """
        self.is_lenovo = is_lenovo
        print(f"Trạng thái Lenovo: {self.is_lenovo}")

    def on_press(self, key):
        """
        Xử lý sự kiện khi nhấn phím
        """
        try:
            # Hoàn nguyên: Chỉ xử lý Double Right Shift
            if key == Key.shift_r:
                current_time = time.time()
                time_diff = current_time - self.last_right_shift_time

                if time_diff < DOUBLE_SPACE_THRESHOLD:
                    self.should_scan = True
                    self.trigger_source = 'double_right_shift'
                    self.last_right_shift_time = 0
                    self.last_backslash_time = 0
                    self.last_num_lock_time = 0
                else:
                    self.last_right_shift_time = current_time
                    self.last_backslash_time = 0
                    self.last_num_lock_time = 0

            elif isinstance(key, keyboard.KeyCode) and key.char == '\\':
                current_time = time.time()
                time_diff = current_time - self.last_backslash_time

                if time_diff < DOUBLE_SPACE_THRESHOLD:
                    self.should_scan = True
                    self.trigger_source = 'double_backslash'

                self.last_backslash_time = current_time
                self.last_right_shift_time = 0
                self.last_num_lock_time = 0

            elif key == Key.scroll_lock:
                self.should_scan = True
                self.trigger_source = 'scroll_lock'
                self.last_right_shift_time = 0
                self.last_backslash_time = 0
                self.last_num_lock_time = 0

            elif key == Key.num_lock:
                current_time = time.time()
                time_diff = current_time - self.last_num_lock_time

                if time_diff < DOUBLE_SPACE_THRESHOLD:
                    self.should_scan = True
                    self.trigger_source = 'double_num_lock'
                    self.last_num_lock_time = 0
                else:
                    self.last_num_lock_time = current_time
                self.last_right_shift_time = 0
                self.last_backslash_time = 0

            else:
                self.last_right_shift_time = 0
                self.last_backslash_time = 0
                self.last_num_lock_time = 0
                if self.space_count > 0:
                    self.space_count = 0

        except AttributeError:
            self.last_right_shift_time = 0
            self.last_backslash_time = 0
            self.last_num_lock_time = 0
            pass
        except Exception as e:
            print(f"Lỗi khi xử lý phím: {str(e)}")

    def start_listening(self):
        """
        Bắt đầu lắng nghe sự kiện bàn phím
        """
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        print("Đã bắt đầu theo dõi bàn phím...")

    def stop_listening(self):
        """
        Dừng lắng nghe sự kiện bàn phím
        """
        if hasattr(self, 'listener') and self.listener:
            self.listener.stop()
            print("Đã dừng theo dõi bàn phím.")
