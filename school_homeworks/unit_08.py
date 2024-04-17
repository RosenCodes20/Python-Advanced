text = ""
with open("file_1.txt", "r") as file_1:
    with open("file_2.txt", "r") as file_2:
        text += file_1.read()
        text += file_2.read()

with open("merged.txt", "a") as merged_file:
    merged_file.write(text)