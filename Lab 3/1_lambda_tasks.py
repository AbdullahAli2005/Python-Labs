# Exercise 1

# 1) Square and cube using lambda
nums = [9, 16, 25]
squares = list(map(lambda x: x**2, nums))
cubes = list(map(lambda x: x**3, nums))
print("Squares:", squares)
print("Cubes:", cubes)

# # 2) Starts with a given character
starts_with = lambda s, ch: s.startswith(ch)
inp = input("Enter a string: ")
print("Starts with A:", starts_with(inp, 'A'))

# # 3) Extract year, month, date and time
from datetime import datetime
now = datetime.now()
extract = lambda dt: (dt.year, dt.month, dt.day, dt.strftime("%H:%M:%S"))
print("Current date & time parts:", extract(now))
