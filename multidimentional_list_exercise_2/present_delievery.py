count_of_presents = int(input())
num = int(input())
matrix = []
santa_positions = []
total_nice_kids = 0
positions = {
    "up": (-1, 0),
    "left": (0, -1),
    "down": (1, 0),
    "right": (0, 1)
}
gifts_for_kids = 0
for rows in range(num):
    matrix.append(input().split())

    if "S" in matrix[rows]:
        santa_positions = [rows, matrix[rows].index("S")]
        matrix[santa_positions[0]][santa_positions[1]] = "-"

    total_nice_kids += matrix[rows].count("V")

command = input()

while command != "Christmas morning":
    santa_positions = [santa_positions[0] + positions[command][0],
                       santa_positions[1] + positions[command][1]
                       ]

    house = matrix[santa_positions[0]][santa_positions[1]]
    if house == "V":
        count_of_presents -= 1
        gifts_for_kids += 1

    elif house == "C":
        for coordinates in positions.values():
            position_row = santa_positions[0] + coordinates[0]
            positions_col = santa_positions[1] + coordinates[1]
            if matrix[position_row][positions_col].isalpha():
                if matrix[position_row][positions_col] == "V":
                    gifts_for_kids += 1

                matrix[position_row][positions_col] = "-"
                count_of_presents -= 1

            if not count_of_presents:
                break

    matrix[santa_positions[0]][santa_positions[1]] = "-"
    if not count_of_presents or total_nice_kids == gifts_for_kids:
        break

    command = input()

matrix[santa_positions[0]][santa_positions[1]] = "S"

if not count_of_presents and gifts_for_kids < total_nice_kids:
    print("Santa ran out of presents!")

print(*[" ".join(line) for line in matrix], sep="\n")

if total_nice_kids == gifts_for_kids:
    print(f'Good job, Santa! {gifts_for_kids} happy nice kid/s.')

else:
    print(f'No presents for {total_nice_kids - gifts_for_kids} nice kid/s.')
