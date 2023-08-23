import os
import time

import pyautogui
from datetime import datetime
from pynput import mouse

class ScreenshotCapture:
    def __init__(self):
        self.running = False

    def screenshot(self):
        screenshot = pyautogui.screenshot()
        screenshot_folder = "../Logs/screenshots"
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        screenshot.save(os.path.join(screenshot_folder, f"screenshot_{timestamp}.png"))

    def on_mouse_click(self, x, y, button, pressed):
        if pressed:
            time.sleep(0.2)
            self.screenshot()

    def start_capture(self):
        print("Screenshot capturing started. Press 'Ctrl+C' to stop.")
        with mouse.Listener(on_click=self.on_mouse_click) as listener:
            self.running = True
            listener.join()

        print("Screenshot capturing stopped.")