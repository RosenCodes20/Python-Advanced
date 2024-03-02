from collections import deque

bomb_effects = deque(int(el) for el in input().split(", "))
bomb_easings = deque(int(el) for el in input().split(", "))

datura = 0
cherry = 0
snake = 0

while bomb_effects and bomb_easings:
    current_effect = bomb_effects.popleft()
    current_easing = bomb_easings.pop()

    current_sum = current_effect + current_easing

    if current_sum == 40:
        datura += 1

    elif current_sum == 60:
        cherry += 1

    elif current_sum == 120:
        snake += 1

    else:
        bomb_effects.appendleft(current_effect)
        bomb_easings.append(current_easing - 5)

    if datura >= 3 and cherry >= 3 and snake >= 3:
        break

if datura >= 3 and cherry >= 3 and snake >= 3:
    print("Bene! You have successfully filled the bomb pouch!")

else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")

else:
    print("Bomb Effects: empty")

if bomb_easings:
    print(f"Bomb Casings: {', '.join(map(str, bomb_easings))}")

else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry}")
print(f"Datura Bombs: {datura}")
print(f"Smoke Decoy Bombs: {snake}")