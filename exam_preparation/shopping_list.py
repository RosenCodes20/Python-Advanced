def shopping_list(budget, **kwargs):
    sum_of_shopping = 1
    result = ""
    basket = 0
    if budget < 100:
        return "You do not have enough budget."

    for product, price in kwargs.items():
        if basket == 5:
            break

        sum_of_shopping = float(price[0]) * int(price[1])

        if sum_of_shopping > budget:
            continue
        else:
            budget -= sum_of_shopping
            result += f"You bought {product} for {sum_of_shopping:.2f} leva.\n"
            basket += 1
    return result


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),)
      )

