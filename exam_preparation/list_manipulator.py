from collections import deque


def list_manipulator(nums_list: list, second_par, third_par, *args):

    if second_par == "add" and third_par == "beginning":
        for element in reversed(args):
            nums_list = deque(nums_list)
            nums_list.appendleft(element)

        return list(nums_list)

    elif second_par == "add" and third_par == "end":
        for element in args:
            nums_list.append(element)

        return list(nums_list)

    elif second_par == "remove" and third_par == "beginning":
        nums_list = deque(nums_list)
        if args:
            num = int(args[0])
            for i in range(num):
                nums_list.popleft()

        elif not args:
            nums_list.popleft()

        return list(nums_list)

    elif second_par == "remove" and third_par == "end":
        nums_list = deque(nums_list)
        if args:
            num = int(args[0])
            for i in range(num):
                nums_list.pop()

        elif not args:
            nums_list.pop()

        return list(nums_list)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
