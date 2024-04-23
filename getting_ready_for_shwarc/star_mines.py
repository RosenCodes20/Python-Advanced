rows, cols = [int(el) for el in input().split(",")]

matrix = [[100] * cols for _ in range(rows)]

col_row = input().split(",")

while col_row[0] != "GAME OVER":
    col = int(col_row[1])
    row = int(col_row[0])
    reduce_damage = int(col_row[2])

    if 0 <= col < cols and 0 <= row < rows:
        matrix[row][col] -= reduce_damage

        for i in range(max(0, row - 1), min(len(matrix), row + 2)):
            for j in range(max(0, col - 1), min(len(matrix[0]), col + 2)):
                if (i, j) != (row, col):
                    matrix[i][j] -= 10
                    matrix[i][j] = max(0, matrix[i][j])

    col_row = input().split(",")

for row in matrix:
    print(" ".join(map(str, row)))