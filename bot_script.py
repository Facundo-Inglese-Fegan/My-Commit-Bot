# bot_script.py
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%Y-%-m-%d %H:%M:%S")

with open("commit_log.txt", "a") as log_file:
    log_file.write(f"Commit made at: {current_time}\n")

print("Log updated successfully.")