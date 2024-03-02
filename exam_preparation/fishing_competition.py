rows = int(input())

matrix = [list(input()) for _ in range(rows)]

my_pos = []

positions = {
    "up": (-1, 0),
    "left": (0, -1),
    "down": (1, 0),
    "right": (0, 1)
}
caught_fish = 0

for row in range(rows):

    if "S" in matrix[row]:
        my_pos = [row, matrix[row].index("S")]
        matrix[my_pos[0]][my_pos[1]] = "-"

command = input()

while command != "collect the nets":
    my_pos = [(my_pos[0] + positions[command][0]) % rows, (my_pos[1] + positions[command][1]) % rows]
    current_position = matrix[my_pos[0]][my_pos[1]]
    matrix[my_pos[0]][my_pos[1]] = "-"
    if current_position == "W":
        caught_fish = 0
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{my_pos[0]},{my_pos[1]}]")
        raise SystemExit

    elif current_position in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        caught_fish += int(current_position)

    command = input()

matrix[my_pos[0]][my_pos[1]] = "S"

if caught_fish >= 20:
    print("Success! You managed to reach the quota!")

else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - caught_fish} tons of fish more.")

if caught_fish > 0:
    print(f"Amount of fish caught: {caught_fish} tons.")


for row in matrix:
    print("".join(row))