from collections import deque

bowls = deque(int(el) for el in input().split(", "))
customers = deque(int(el) for el in input().split(", "))

while bowls and customers:
    current_bowl = bowls.pop()
    current_customer = customers.popleft()

    if current_bowl == current_customer:
        continue

    elif current_bowl > current_customer:
        current_bowl -= current_customer
        bowls.append(current_bowl)

    elif current_bowl < current_customer:
        current_customer -= current_bowl
        customers.appendleft(current_customer)

if not customers:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(map(str, bowls))}")

elif not bowls:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join(map(str, customers))}")
