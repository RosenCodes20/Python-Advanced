from collections import deque

expression = deque(input().split())
cur_idx = 0

while cur_idx < len(expression):
    current_element = expression[cur_idx]

    if current_element == "*":
        for i in range(cur_idx - 1):
            expression.appendleft(int(expression.popleft()) * int(expression.popleft()))

    elif current_element == "+":
        for i in range(cur_idx - 1):
            expression.appendleft(int(expression.popleft()) + int(expression.popleft()))

    elif current_element == "-":
        for i in range(cur_idx - 1):
            expression.appendleft(int(expression.popleft()) - int(expression.popleft()))

    elif current_element == "/":
        for i in range(cur_idx - 1):
            expression.appendleft(int(expression.popleft()) / int(expression.popleft()))

    if current_element == "+" or current_element == "-" or current_element == "/" or current_element == "*":
        del expression[1]
        cur_idx = 1
    cur_idx += 1

print(round(int(expression[0])))

