import datetime
import re

year = int(input())
day = int(input())

date_to_format = []

date = str(datetime.date(year, 1, 1) + datetime.timedelta(day - 1))

nums = re.findall(r"[0-9]+", date)

day = nums[2]
month = nums[1]
years = nums[0]

print(f"{day}.{month}.{years}")

