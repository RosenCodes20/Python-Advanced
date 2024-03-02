from collections import deque

armor = deque(int(el) for el in input().split(","))
striking_impact = deque(int(el) for el in input().split(","))

killed_monsters = 0
while armor and striking_impact:
    current_armor = armor.popleft()
    current_impact = striking_impact.pop()

    if current_impact >= current_armor:
        killed_monsters += 1
        current_impact -= current_armor

        if striking_impact:
            striking_impact[-1] += current_impact

        elif not striking_impact and current_impact > 0:
            striking_impact.append(current_impact)

    else:
        current_armor -= current_impact
        armor.append(current_armor)

if not armor:
    print("All monsters have been killed!")

if not striking_impact:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")