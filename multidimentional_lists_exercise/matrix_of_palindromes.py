rows, cols = [int(el) for el in input().split()]

start = ord("a")

for row in range(start, rows + start):
    for col in range(row, row + cols):
        print(f"{chr(row)}{chr(col)}{chr(row)}", end=" ", )

    print()