from browser_history import browsers
import os

Browser = [browsers.Firefox, browsers.Chrome, browsers.Safari, browsers.Brave, browsers.Opera, browsers.Edge]

for Br in Browser:
    try:
        browser_instance = Br()
        history_entries = browser_instance.fetch_history()
    except Exception as ex:
        print(f"Error fetching history from {Br.name}: {ex}")
        continue

    # print(history_entries)

    if history_entries:
        history_folder = "Browser_History"

        # creating the folder "Browser_History" to store the browser history files
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
