rows = int(input())

matrix = [list(input()) for _ in range(rows)]

positions = {
    "up": (-1, 0),
    "left": (0, -1),
    "down": (1, 0),
    "right": (0, 1)
}

submarine_position = []
hit_times = 3
battle_cruisers = 0
for rows_index in range(rows):
    if "S" in matrix[rows_index]:
        submarine_position = [rows_index, matrix[rows_index].index("S")]
        matrix[submarine_position[0]][submarine_position[1]] = "-"
    battle_cruisers += matrix[rows_index].count("C")

command = input()
while hit_times > 0 and battle_cruisers > 0:
    submarine_position = [submarine_position[0] + positions[command][0], submarine_position[1] + positions[command][1]]
    current_position = matrix[submarine_position[0]][submarine_position[1]]

    if current_position == "*":
        matrix[submarine_position[0]][submarine_position[1]] = "-"
        hit_times -= 1
        if hit_times <= 0:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_position[0]}, {submarine_position[1]}]!")
            break

    elif current_position == "C":
        matrix[submarine_position[0]][submarine_position[1]] = "-"
        battle_cruisers -= 1
        if battle_cruisers <= 0:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break
    command = input()

matrix[submarine_position[0]][submarine_position[1]] = "S"

[print("".join(row)) for row in matrix]