from string import punctuation

with open("text.txt", "r") as text_file:
    file = text_file.readlines()

with open("output.txt", "w") as output_file:
    for row in range(len(file)):
        letters = 0
        punctuations_mark = 0

        for element in file[row]:
            if element.isalpha():
                letters += 1

            elif element in punctuation:
                punctuations_mark += 1

        output_file.write(f"Line {row + 1}: {''.join(file[row])[:-1]} ({letters})({punctuations_mark})\n")
