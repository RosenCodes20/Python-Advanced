from collections import deque

egg_size = deque(int(el) for el in input().split(", "))
paper_size = deque(int(el) for el in input().split(", "))
boxes = 0
while egg_size and paper_size:
    current_egg = egg_size.popleft()
    current_paper = paper_size.pop()
    products_sum = current_paper + current_egg
    if current_egg <= 0:
        paper_size.append(current_paper)
        continue

    elif current_egg == 13:
        first_paper = paper_size.popleft()
        last_paper = current_paper
        paper_size.append(first_paper)
        paper_size.appendleft(last_paper)

    elif products_sum <= 50:
        boxes += 1

if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")

else:
    print("Sorry! You couldn't fill any boxes!")

if egg_size:
    print(f"Eggs left: {', '.join(map(str, egg_size))}")

if paper_size:
    print(f"Pieces of paper left: {', '.join(map(str, paper_size))}")