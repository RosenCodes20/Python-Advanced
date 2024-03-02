rows, cols = [int(el) for el in input().split()]

matrix = [list(input()) for _ in range(rows)]
pos_delivery_boy = []

positions = {
    "up": (-1, 0),
    "left": (0, -1),
    "down": (1, 0),
    "right": (0, 1)
}

for rows_index in range(rows):

    if "B" in matrix[rows_index]:
        pos_delivery_boy = [rows_index, matrix[rows_index].index("B")]
        break

while True:
    command = input()
    pos_delivery_boy = [pos_delivery_boy[0] + positions[command][0], pos_delivery_boy[1] + positions[command][1]]
    current_position = matrix[pos_delivery_boy[0]][pos_delivery_boy[1]]

    if 0 <= pos_delivery_boy[0] < cols and 0 <= pos_delivery_boy[1] < cols:
        if current_position == "*":
            print("The delivery is late. Order is canceled.")

        else:
            matrix[pos_delivery_boy[0]][pos_delivery_boy[1]] = "."

            if current_position == "P":
                matrix[pos_delivery_boy[0]][pos_delivery_boy[1]] = "R"
                print("Pizza is collected. 10 minutes for delivery.")

            elif current_position == "A":
                matrix[pos_delivery_boy[0]][pos_delivery_boy[1]] = "P"
                print("Pizza is delivered on time! Next order...")
                break
    else:
        print("The delivery is late. Order is canceled.")
        break

[print("".join(row)) for row in matrix]
