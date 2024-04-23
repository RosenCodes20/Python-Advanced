nums = input().split("|")

flatten_list = []

for num in nums[::-1]:
    current_num = num.split()
    flatten_list.extend(current_num)

print(*flatten_list)