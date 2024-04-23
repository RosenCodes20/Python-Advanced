num = int(input())
knight_matrix = [list(input()) for _ in range(num)]

positions = (
    (-2, -1),
    (-2, 1),
    (2, -1),
    (2, 1),
    (-1, 2),
    (-1, -2),
    (1, 2),
    (1, -2)
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_best_position = []

    for row in range(num):
        for col in range(num):
            if knight_matrix[row][col] == "K":
                knight_attacks = 0

                for position in positions:
                    position_row = row + position[0]
                    position_col = col + position[1]

                    if 0 <= position_row < num and 0 <= position_col < num:
                        if knight_matrix[position_row][position_col] == "K":
                            knight_attacks += 1

                if knight_attacks > max_attacks:
                    max_attacks = knight_attacks
                    knight_with_best_position = [row, col]

    if knight_with_best_position:
        knight_r, knight_c = knight_with_best_position
        knight_matrix[knight_r][knight_c] = "0"
        removed_knights += 1

    else:
        break

print(removed_knights)