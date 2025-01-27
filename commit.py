import os
import datetime

# File to modify daily
filename = "daily.txt"

# Update the file with today's date
with open(filename, "a") as file:
    file.write(f"Commit on {datetime.datetime.now().isoformat()}\n")

# Stage the file
os.system("git add .")

# Commit with a message
os.system(f'git commit -m "Daily commit for {datetime.datetime.now().date()}"')
