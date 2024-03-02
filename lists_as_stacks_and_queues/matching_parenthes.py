parentheses = input()
parentheses_stack = []
for i in range(0, len(parentheses)):

    if parentheses[i] == "(":
        parentheses_stack.append(i)

    elif parentheses[i] == ")":
        start_index = parentheses_stack.pop()
        end_index = i + 1

        print(parentheses[start_index: end_index])