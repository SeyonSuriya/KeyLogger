import keyboard
import pyperclip
import time
from datetime import datetime

class ClipboardMonitor:
    def __init__(self, interval=1):
        self.interval = interval
        self.previous_clipboard_content = pyperclip.paste()

    def save_clipboard_content(self, content):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        content_to_save = f"{now.date()} - {now.time()} - \n{content}\n"

        with open("../Logs/clipboard_grap.txt", "a") as file:
            file.write(content_to_save)
            file.write("\n")

    def start_monitoring(self):
        print("Clipboard monitoring started. Press 'Ctrl+C' to stop.")
        try:
            while True:
                clipboard_content = pyperclip.paste()
                if clipboard_content != self.previous_clipboard_content:
                    self.previous_clipboard_content = clipboard_content
                    self.save_clipboard_content(clipboard_content)
                    print("New clipboard content saved.")
                time.sleep(self.interval)
                if keyboard.is_pressed('ctrl') and keyboard.is_pressed('shift') and keyboard.is_pressed('alt'):
                    print("Clipboard monitoring stopped.")
                    break  # Exit the loop when the key combination is pressed
        except KeyboardInterrupt:
            print("Clipboard monitoring stopped.")