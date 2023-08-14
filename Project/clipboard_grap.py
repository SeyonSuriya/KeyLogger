import pyperclip
import time
from datetime import datetime

# Initialize the previous clipboard content
previous_clipboard_content = pyperclip.paste()

def save_clipboard_content(content):
    # Get current date and time
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    # Prepare content with date, time, and grabbed content
    content_to_save = f"{now.date()} - {now.time()} - \n{content}\n"

    # Save content to the "clipboard.txt" file
    with open("clipboard_grap.txt", "a") as file:
        file.write(content_to_save)

print("Clipboard monitoring started. Press 'Ctrl+C' to stop.")

try:
    while True:
        clipboard_content = pyperclip.paste()
        if clipboard_content != previous_clipboard_content:
            previous_clipboard_content = clipboard_content
            save_clipboard_content(clipboard_content)
            print("New clipboard content saved.")
        time.sleep(1)  # Adjust the interval as needed
except KeyboardInterrupt:
    print("Clipboard monitoring stopped.")
