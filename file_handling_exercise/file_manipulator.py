import os

command = input().split("-")

while command[0] != "End":
    if command[0] == "Create":
        file_name = command[1]
        with open(file_name, "w") as new_text_file:
            pass

    elif command[0] == "Add":
        file_name = command[1]
        content = command[2]
        with open(file_name, "a") as new_text_file:
            new_text_file.write(f"{content}\n")

    elif command[0] == "Replace":
        file_name = command[1]
        old_string = command[2]
        new_string = command[3]
        try:
            with open(file_name, "r+") as new_text_file:
                current_file = new_text_file.read()
                current_file = current_file.replace(old_string, new_string)
                new_text_file.seek(0)
                new_text_file.write(current_file)
                new_text_file.truncate()

        except FileNotFoundError:
            print("An error occurs!")

    elif command[0] == "Delete":
        file_name = command[1]
        try:
            os.remove(file_name)

        except FileNotFoundError:
            print("An error occurs!")

    command = input().split("-")

