import os

ABSOLUTE_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
file_name = "text.txt"

path = os.path.join(ABSOLUTE_DIR_PATH, file_name)

try:
    open_file = open(path)
    print("File found!")


except FileNotFoundError:
    print("File not found!")

finally:
    print("Exiting!")