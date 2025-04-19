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
        self.trigger_source = None
        self.is_lenovo = False

    def set_lenovo_status(self, is_lenovo):
        self.is_lenovo = is_lenovo

    def on_press(self, key):
        try:
            # Xử lý Double Right Shift - chỉ cho máy Lenovo
            if key == Key.shift_r and self.is_lenovo:
                current_time = time.time()
                time_diff = current_time - self.last_right_shift_time

                if time_diff < DOUBLE_SPACE_THRESHOLD:
                    self.should_scan = True
                    self.trigger_source = 'double_right_shift'

                self.last_right_shift_time = current_time

            elif isinstance(key, keyboard.KeyCode) and key.char == '\\':
                current_time = time.time()
                time_diff = current_time - self.last_backslash_time

                if time_diff < DOUBLE_SPACE_THRESHOLD:
                    self.should_scan = True
                    self.trigger_source = 'double_backslash'

                self.last_backslash_time = current_time

            elif key == Key.scroll_lock:
                self.should_scan = True
                self.trigger_source = 'scroll_lock'

            else:
                if self.space_count > 0:
                    self.space_count = 0

        except AttributeError:
            pass

    def start_listening(self):
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def stop_listening(self):
        if hasattr(self, 'listener'):
            self.listener.stop()
