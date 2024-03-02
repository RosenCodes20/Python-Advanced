from functools import reduce


def operate(operator, *args):
    if operator == "+":
        return reduce(lambda num1, num2: num1 + num2, args)

    elif operator == "-":
        return reduce(lambda num1, num2: num1 - num2, args)

    elif operator == "/":
        return reduce(lambda num1, num2: num1 / num2, args)

    elif operator == "*":
        return reduce(lambda num1, num2: num1 * num2, args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
