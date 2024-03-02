n, m = [int(el) for el in input().split(",")]

matrix = [list(input()) for _ in range(n)]
mouse_position = []
positions = {
    "up": (-1, 0),
    "left": (0, -1),
    "down": (1, 0),
    "right": (0, 1)
}
cheese_count = 0
for rows in range(n):

    if "M" in matrix[rows]:
        mouse_position = [rows, matrix[rows].index("M")]
        matrix[mouse_position[0]][mouse_position[1]] = "*"

    cheese_count += matrix[rows].count("C")

command = input()

while command != "danger":
    mouse_position = [mouse_position[0] + positions[command][0], mouse_position[1] + positions[command][1]]

    if 0 <= mouse_position[0] < n and 0 <= mouse_position[1] < m:
        current_position = matrix[mouse_position[0]][mouse_position[1]]
        matrix[mouse_position[0]][mouse_position[1]] = "*"

        if current_position == "C":
            cheese_count -= 1
            if cheese_count <= 0:
                print("Happy mouse! All the cheese is eaten, good night!")
                break

        elif current_position == "T":
            print("Mouse is trapped!")
            break

        elif current_position == "@":
            matrix[mouse_position[0]][mouse_position[1]] = "@"
            mouse_position = [mouse_position[0] - positions[command][0], mouse_position[1] - positions[command][1]]

    else:
        mouse_position = [mouse_position[0] - positions[command][0], mouse_position[1] - positions[command][1]]
        print("No more cheese for tonight!")
        break

    command = input()

if command == "danger":
    print("Mouse will come back later!")
    
matrix[mouse_position[0]][mouse_position[1]] = "M"

[print("".join(row)) for row in matrix]