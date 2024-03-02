from collections import deque

firework_effects = deque(int(el) for el in input().split(", "))
explosive_power = deque(int(el) for el in input().split(", "))

palm = 0
willow = 0
crossette = 0

while firework_effects and explosive_power:
    current_firework = firework_effects.popleft()
    current_power = explosive_power.pop()

    if current_firework <= 0:
        explosive_power.append(current_power)
        continue

    elif current_power <= 0:
        firework_effects.appendleft(current_firework)
        continue

    current_sum = current_firework + current_power

    if current_sum % 3 == 0 and current_sum % 5 != 0:
        palm += 1

    elif current_sum % 5 == 0 and current_sum % 3 != 0:
        willow += 1

    elif current_sum % 5 == 0 and current_sum % 3 == 0:
        crossette += 1

    else:
        current_firework -= 1
        firework_effects.append(current_firework)
        explosive_power.append(current_power)

    if palm >= 3 and willow >= 3 and crossette >= 3:
        print("Congrats! You made the perfect firework show!")
        break

else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")