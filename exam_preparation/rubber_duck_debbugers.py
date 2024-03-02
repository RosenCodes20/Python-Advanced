from collections import deque

time = deque(int(el) for el in input().split())
tasks = deque(int(el) for el in input().split())

darth_vader = 0
thor = 0
big_blue = 0
small_yellow = 0
while time and tasks:

    current_time = time.popleft()
    current_task_time = tasks.pop()

    multiply_of_elements = current_time * current_task_time

    if 0 < multiply_of_elements <= 60:
        darth_vader += 1

    elif 60 < multiply_of_elements <= 120:
        thor += 1

    elif 120 < multiply_of_elements <= 180:
        big_blue += 1

    elif 180 < multiply_of_elements <= 240:
        small_yellow += 1

    else:
        current_task_time -= 2
        time.append(current_time)
        tasks.append(current_task_time)


print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

print(f"Darth Vader Ducky: {darth_vader}")
print(f"Thor Ducky: {thor}")
print(f"Big Blue Rubber Ducky: {big_blue}")
print(f"Small Yellow Rubber Ducky: {small_yellow}")