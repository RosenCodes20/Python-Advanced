from collections import deque

tools = deque(int(el) for el in input().split())
substances = deque(int(el) for el in input().split())
challenges = deque(int(el) for el in input().split())

while tools and substances:
    current_tool = tools.popleft()
    current_substance = substances.pop()

    current_multiply = current_tool * current_substance

    if current_multiply in challenges:
        challenges.remove(current_multiply)

    elif current_multiply not in challenges:
        current_tool += 1
        tools.append(current_tool)
        current_substance -= 1
        if current_substance > 0:
            substances.append(current_substance)

    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break

    elif challenges and not substances or not tools:
        print("Harry is lost in the temple. Oblivion awaits him.")
        break

if tools:
    print(f"Tools: {', '.join(map(str, tools))}")

if substances:
    print(f"Substances: {', '.join(map(str, substances))}")

if challenges:
    print(f"Challenges: {', '.join(map(str, challenges))}")