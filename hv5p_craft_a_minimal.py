import os
import time
from plyer import notification

def notify(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,  # e.g. '/path/to/icon_ico.ico'
        timeout = 10,  # seconds
    )

def automation_script_notifier(script_path, interval=60):
    while True:
        if os.path.exists(script_path):
            notify("Script Alert", f"Script '{os.path.basename(script_path)}' has finished running.")
            break
        time.sleep(interval)

if __name__ == "__main__":
    script_path = input("Enter the path to your automation script: ")
    automation_script_notifier(script_path)