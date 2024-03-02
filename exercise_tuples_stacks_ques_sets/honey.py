from collections import deque

bees = deque([int(el) for el in input().split()])
honey = [int(el) for el in input().split()]
symbols = deque(input().split())

total_sum = 0

while bees and honey:

    current_bee = bees.popleft()
    current_nectar = honey.pop()

    if current_nectar >= current_bee:
        current_symbol = symbols.popleft()

        if current_symbol == "*":
            total_sum += abs(current_bee * current_nectar)

        elif current_symbol == "+":
            total_sum += abs(current_bee + current_nectar)

        elif current_symbol == "/":
            total_sum += abs(current_bee / current_nectar) if current_nectar != 0 else 0

        elif current_symbol == "-":
            total_sum += abs(current_bee - current_nectar)

    elif current_nectar < current_bee:
        bees.appendleft(current_bee)

print(f"Total honey made: {total_sum}")

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")

if honey:
    print(f"Honey left: {', '.join(map(str, honey))}")