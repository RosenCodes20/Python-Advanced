from collections import deque

males = deque(int(el) for el in input().split())
females = deque(int(el) for el in input().split())

matches = 0

while males and females:
    first_female = females.popleft()
    last_male = males.pop()

    if first_female <= 0:
        males.append(last_male)
        continue

    if first_female % 25 == 0:
        females.popleft()

    if last_male <= 0:
        females.appendleft(first_female)
        continue

    if last_male % 25 == 0:
        males.pop()

    if first_female == last_male:
        matches += 1

    elif first_female != last_male:
        if last_male > 0:
            males.append(last_male - 2)


print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join(map(str, reversed(males)))}")

else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(map(str, females))}")

else:
    print("Females left: none")