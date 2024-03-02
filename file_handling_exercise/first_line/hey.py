import os


directory = input()
extensions_dict = {}
is_dir = False
try:
    for filename in os.listdir(directory):
        current_file = os.path.join(directory, filename)

        if os.path.isfile(current_file):
            extension = filename.split(".")[-1]

            if extension not in extensions_dict:
                extensions_dict[extension] = []

            extensions_dict[extension].append(filename)

        elif os.path.isdir(current_file) and not is_dir:
            is_dir = True

    for extension, file_name in sorted(extensions_dict.items(), key=lambda x: x[0]):
        with open("report.txt", "w") as report_file:
            report_file.write(f".{extension}")

            for name in sorted(file_name):
                report_file.write(f"- - - {name}")

except FileNotFoundError:
    print("Directory not found please enter one again!")