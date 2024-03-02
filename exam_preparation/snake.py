rows = int(input())

matrix = [list(input()) for _ in range(rows)]

positions = {
    "up": (-1, 0),
    "left": (0, -1),
    "down": (1, 0),
    "right": (0, 1)
}
snake_pos = []
food = 0
for row in range(rows):
    if "S" in matrix[row]:
        snake_pos = [row, matrix[row].index("S")]
        matrix[snake_pos[0]][snake_pos[1]] = "."

command = input()

while food < 10:
    snake_pos = [snake_pos[0] + positions[command][0], snake_pos[1] + positions[command][1]]

    if 0 <= snake_pos[0] < rows and 0 <= snake_pos[1] < rows:
        current_position = matrix[snake_pos[0]][snake_pos[1]]
        matrix[snake_pos[0]][snake_pos[1]] = "."

        if current_position == "*":
            food += 1

        elif current_position == "B":
            for row in range(rows):
                if "B" in matrix[row]:
                    snake_pos = [row, matrix[row].index("B")]
                    matrix[snake_pos[0]][snake_pos[1]] = "."

    elif not (0 <= snake_pos[0] < rows and 0 <= snake_pos[1] < rows):
        print(f"Game over!")
        break

    if food >= 10:
        print("You won! You fed the snake.")
        break

    command = input()

if 0 <= snake_pos[0] < rows and 0 <= snake_pos[1] < rows:
    matrix[snake_pos[0]][snake_pos[1]] = "S"

print(f"Food eaten: {food}")

[print("".join(row)) for row in matrix]