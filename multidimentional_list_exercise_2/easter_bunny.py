import sys

size_of_the_field = int(input())
matrix = [input().split() for _ in range(size_of_the_field)]
best_direction = []
best_path = None
max_eggs = -sys.maxsize
bunny_position = []
positions = {
    "up": (-1, 0),
    "left": (0, -1),
    "down": (1, 0),
    "right": (0, 1)
}

for row in range(size_of_the_field):
    if "B" in matrix[row]:
        bunny_position = [row, matrix[row].index("B")]

for direction, position in positions.items():
    position_row = bunny_position[0] + position[0]
    position_col = bunny_position[1] + position[1]

    collected_eggs = 0
    path = []

    while 0 <= position_row < size_of_the_field and 0 <= position_col < size_of_the_field:

        if matrix[position_row][position_col] == "X":
            break

        else:
            collected_eggs += int(matrix[position_row][position_col])
            path.append([position_row, position_col])

        position_row += position[0]
        position_col += position[1]

    if collected_eggs >= max_eggs:
        max_eggs = collected_eggs
        best_path = path
        best_direction = direction

print(best_direction)
print("\n".join(map(str, best_path)))
print(max_eggs)