import os
import pyautogui
import threading
import keyboard
from datetime import datetime

# Global variables
running = True
screenshot_count = 0

def screenshot_thread():
    global running, screenshot_count
    while running:
        if screenshot_count > 0:
            # Capture screenshot
            screenshot = pyautogui.screenshot()
            # Create the "screenshots" directory if it doesn't exist
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            # Get current date and time
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
            # Save screenshot within the "screenshots" directory with the timestamp as the name
            screenshot.save(os.path.join("screenshots", f"screenshot_{timestamp}.png"))
            screenshot_count -= 1

def stop_screenshot_thread():
    global running
    running = False

# Start the screenshot thread
thread = threading.Thread(target=screenshot_thread)
running = True
thread.start()

print("Screenshot capturing started. Press 'Esc' to stop.")

# Register the "Esc" key press event
keyboard.on_press_key("esc", stop_screenshot_thread)

# Keep the main thread alive
try:
    while running:
        pass
except KeyboardInterrupt:
    pass

# Stop the screenshot thread
thread.join()
print("Screenshot capturing stopped.")

# Unregister the key press event
keyboard.unhook_all()
