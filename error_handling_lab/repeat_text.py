text = input()

try:
    times = int(input())
    text /= times
    print(text)

except (ValueError, ZeroDivisionError, TypeError):
    print("Variable must be an integer!")
    print("You can't divide by zero!")
