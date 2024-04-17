import os
from datetime import datetime

try:
    os.remove("temp.txt")

except FileNotFoundError:
    print("File not found!")

with open("temp.txt", "a") as temp_file:
    now = datetime.now()
    temp_file.write(f"Current time: {now.strftime('%H:%M:%S')}")