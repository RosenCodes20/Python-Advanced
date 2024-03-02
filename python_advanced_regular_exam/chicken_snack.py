from collections import deque

money = [int(el) for el in input().split()]
prices_of_foods = deque(int(el) for el in input().split())
bought_foods = 0
pocket = 0
while money and prices_of_foods:
    last_money = money.pop()
    first_price = prices_of_foods.popleft()

    if last_money == first_price:
        bought_foods += 1

    elif last_money > first_price:
        bought_foods += 1
        change = last_money - first_price
        if money:
            money[-1] += change
    elif last_money < first_price:
        pass

if bought_foods >= 4:
    print(f"Gluttony of the day! Henry ate {bought_foods} foods.")

elif bought_foods > 1:
    print(f"Henry ate: {bought_foods} foods.")

elif bought_foods == 1:
    print(f"Henry ate: {bought_foods} food.")

elif bought_foods <= 0:
    print(f"Henry remained hungry. He will try next weekend again.")