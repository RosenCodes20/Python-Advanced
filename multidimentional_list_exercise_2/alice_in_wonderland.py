size = int(input())
matrix = [input().split() for _ in range(size)]
alice_position = []

positions = {
    "up": (-1, 0),
    "left": (0, -1),
    "down": (1, 0),
    "right": (0, 1)
}
tea_bags = 0
for row in range(size):
    if "A" in matrix[row]:
        alice_position = [row, matrix[row].index("A")]
        matrix[alice_position[0]][alice_position[1]] = "*"

while tea_bags < 10:
    direction = input()
    position_row = positions[direction][0] + alice_position[0]
    position_col = positions[direction][1] + alice_position[1]

    if not (0 <= position_row < size and 0 <= position_col < size):
        break

    alice_position = [position_row, position_col]
    position = matrix[position_row][position_col]
    matrix[position_row][position_col] = "*"

    if position == "R":
        break

    if position.isdigit():
        tea_bags += int(position)


if tea_bags < 10:
    print("Alice didn't make it to the tea party.")

else:
    print("She did it! She went to the party.")

[print(*element) for element in matrix]