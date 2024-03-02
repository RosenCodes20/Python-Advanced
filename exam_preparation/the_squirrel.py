rows = int(input())

position = input().split(", ")

matrix = [list(input()) for _ in range(rows)]

hazelnuts = 0

positions = {
    "up": (-1, 0),
    "left": (0, -1),
    "down": (1, 0),
    "right": (0, 1)
}
asterix_pos = []
for row in range(rows):

    if "s" in matrix[row]:
        asterix_pos = [row, matrix[row].index("s")]

is_trap = False

for command in position:
    asterix_pos = [asterix_pos[0] + positions[command][0], asterix_pos[1] + positions[command][1]]
    if 0 <= asterix_pos[0] < rows and 0 <= asterix_pos[1] < rows:
        current_position = matrix[asterix_pos[0]][asterix_pos[1]]
        matrix[asterix_pos[0]][asterix_pos[1]] = "*"

        if current_position == "h":
            hazelnuts += 1

        elif current_position == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            is_trap = True
            break

    elif not (0 <= asterix_pos[0] < rows and 0 <= asterix_pos[1] < rows):
        is_trap = True
        print("The squirrel is out of the field.")
        break

if not is_trap:
    if hazelnuts < 3:
        print("There are more hazelnuts to collect.")

    elif hazelnuts >= 3:
        print("Good job! You have collected all hazelnuts!")

print(f"Hazelnuts collected: {hazelnuts}")
