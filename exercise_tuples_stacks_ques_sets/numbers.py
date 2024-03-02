first_nums = set([int(el) for el in input().split()])
second_nums = set([int(el) for el in input().split()])

for i in range(int(input())):

    command, command_type, *nums = input().split()
    nums = set(map(int, nums))

    if command == "Add":

        if command_type == "First":
            first_nums.update(nums)

        elif command_type == "Second":
            second_nums.update(nums)


    elif command == "Remove":

        if command_type == "First":
            first_nums.difference_update(nums)

        elif command_type == "Second":
            second_nums.difference_update(nums)

    elif command == "Check" and command_type == "Subset":

        if first_nums.issubset(second_nums) or second_nums.issubset(first_nums):
            print(True)

        else:
            print(False)

print(", ".join(map(str, sorted(first_nums))))
print(", ".join(map(str, sorted(second_nums))))
