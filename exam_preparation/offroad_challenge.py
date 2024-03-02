from collections import deque

initial_fuel = deque(int(el) for el in input().split())
additional_index = deque(int(el) for el in input().split())
needed_fuel = deque(int(el) for el in input().split())

attitude = 1
reached = []
while True:
    last_fuel = initial_fuel.pop()
    first_index = additional_index.popleft()
    first_needed_fuel = needed_fuel.popleft()
    current_result = last_fuel - first_index

    if current_result >= first_needed_fuel:
        print(f"John has reached: Altitude {attitude}")
        reached.append(f"Altitude {attitude}")
        attitude += 1

    elif current_result < first_needed_fuel:
        print(f"John did not reach: Altitude {attitude}")
        break


if reached and current_result < first_needed_fuel:
    print(f"John failed to reach the top.\nReached altitudes: {', '.join(reached)}")

elif not reached and current_result < first_needed_fuel:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")

else:
    print("John has reached all the altitudes and managed to reach the top!")