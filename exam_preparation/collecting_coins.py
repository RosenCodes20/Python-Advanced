from math import floor

size = int(input())

matrix = [input().split() for _ in range(size)]
coins = 0
positions = {
    "up": (-1, 0),
    "left": (0, -1),
    "down": (1, 0),
    "right": (0, 1)
}
my_pos = []
my_path = []

for rows in range(size):

    if "P" in matrix[rows]:
        my_pos = [rows, matrix[rows].index("P")]
        my_path.append(my_pos)

command = input()

while coins < 100:
    my_pos = [(my_pos[0] + positions[command][0]) % size, (my_pos[1] + positions[command][1]) % size]
    my_path.append(my_pos)
    current_position = matrix[my_pos[0]][my_pos[1]]
    matrix[my_pos[0]][my_pos[1]] = "-"

    if current_position.isdigit():
        coins += int(current_position)

    elif current_position == "X":
        coins -= coins * (50 / 100)
        print(f"Game over! You've collected {floor(coins)} coins.")
        break

    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        break

    command = input()


print(f"Your path:")
print("\n".join(map(str, my_path)))