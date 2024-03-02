from collections import deque

jobs = deque(int(el) for el in input().split(", "))
index = int(input())

tuple_jobs = [(idx, job) for idx, job in enumerate(jobs)]
sorted_jobs = sorted(tuple_jobs, key=lambda x: (x[1], x[0]))

total_cycles = 0
target_cycles = 0

for curr_index, job in sorted_jobs:
    total_cycles += int(job)

    if curr_index == index:
        target_cycles = total_cycles
        break

print(target_cycles)