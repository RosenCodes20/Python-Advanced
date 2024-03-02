from collections import deque

seats = input().split(", ")
nums = deque(int(el) for el in input().split(", "))
second_nums = deque(int(el) for el in input().split(", "))
rotations = 0
seat_matches = []
while len(seat_matches) < 3 and rotations < 10:
    first_num = nums.popleft()
    last_num = second_nums.pop()

    ascii_character = chr(first_num + last_num)
    first_num_to_search = f"{first_num}{ascii_character}"
    last_num_to_search = f"{last_num}{ascii_character}"

    if first_num_to_search in seats or last_num_to_search in seats:
        seat_matches.append(first_num_to_search if first_num_to_search in seats else last_num_to_search)
        seats.remove(first_num_to_search if first_num_to_search in seats else last_num_to_search)
        rotations += 1
    else:
        nums.append(first_num)
        second_nums.appendleft(last_num)
        rotations += 1

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")