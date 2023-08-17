from browser_history import browsers
import os

class BrowserHistoryFetcher:
    def __init__(self):
        self.browsers = [browsers.Firefox, browsers.Chrome, browsers.Safari, browsers.Brave, browsers.Opera,
                         browsers.Edge]

    def fetch_and_save_history(self):
        for Br in self.browsers:
            try:
                browser_instance = Br()
                history_entries = browser_instance.fetch_history()
            except Exception as ex:
                print(f"Error fetching history from {Br.name}: {ex}")
                continue

            if history_entries:
                history_folder = "../Logs/Browser_History"

                if not os.path.exists(history_folder):
                    os.makedirs(history_folder)

                with open(os.path.join(history_folder + "/", Br.name + "_history.txt"), "a") as file:
                    file.write("\n")
                    entries = history_entries.histories
                    for entry in entries:
                        file.write(f"{entry[0]} - {entry[1]}\n")
                print(Br.name + " history saved to " + Br.name + "_history.txt")
            else:
                print("No " + Br.name + " history found.")