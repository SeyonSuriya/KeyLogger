import os
import pyautogui
import threading
from datetime import datetime
from pynput import mouse, keyboard

class ScreenshotCapture:
    def __init__(self):
        self.running = False
        self.stop_event = threading.Event()  # Event to signal thread to stop

    def screenshot_thread(self):
        while self.running:
            screenshot = pyautogui.screenshot()
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
            screenshot.save(os.path.join("screenshots", f"screenshot_{timestamp}.png"))

    def stop_capture(self, key):
        if key == keyboard.Key.esc:
            self.running = False
            print("Stopping screenshot capturing...")
            return False  # Stop listener

    def start_capture(self):
        print("Screenshot capturing started. Press 'Esc' to stop.")
        with keyboard.Listener(on_press=self.stop_capture) as listener:
            with mouse.Listener(on_click=self.on_mouse_click) as listener_mouse:
                self.running = True
                listener.join()
                listener_mouse.join()

        print("Screenshot capturing stopped.")

    def on_mouse_click(self, x, y, button, pressed):
        if self.running and pressed:
            screenshot = pyautogui.screenshot()
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
            screenshot.save(os.path.join("screenshots", f"screenshot_{timestamp}.png"))

if __name__ == "__main__":
    screenshot_capture = ScreenshotCapture()
    screenshot_capture.start_capture()
