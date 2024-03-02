from collections import deque
chocolates = deque([int(el) for el in input().split(", ")])
milk = deque([int(el) for el in input().split(", ")])
milkshakes = 0
while chocolates and milk and milkshakes != 5:

    current_chocolate = chocolates.pop()
    current_milkshake = milk.popleft()

    if current_milkshake <= 0 and current_chocolate <= 0:
        continue

    elif current_chocolate <= 0:
        milk.appendleft(current_milkshake)
        continue

    elif current_milkshake <= 0:
        chocolates.append(current_chocolate)
        continue

    if current_milkshake == current_chocolate:
        milkshakes += 1

    else:
        milk.append(current_milkshake)
        chocolates.append(current_chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")

else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")

else:
    print("Chocolate: empty")

if milk:
    print(f"Milk: {', '.join(map(str, milk))}")

else:
    print("Milk: empty")