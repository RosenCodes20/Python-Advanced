from collections import deque


def stock_availability(nums_list, second_par, *args):
    if second_par == "delivery":
        for element in args:
            nums_list.append(element)

        return list(nums_list)

    elif second_par == "sell":
        if args:
            for current_element in args:

                if isinstance(current_element, str):
                    if current_element in nums_list:
                        nums_list = [item for item in nums_list if item != current_element]

                elif current_element in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    for i in range(int(current_element)):
                        nums_list = deque(nums_list)
                        nums_list.popleft()

        elif not args:
            nums_list = deque(nums_list)
            nums_list.popleft()

        return list(nums_list)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
