# Exercise 3: Module 

# 1
import math, random, time, glob

print("Square root of 16:", math.sqrt(16))
print("Random integer between 1 and 10:", random.randint(1, 10))

# 2 using alias
import math as maths
print("9 sqrt using alias:", maths.sqrt(9))

# 4 time module
now = time.time()
print("Current timestamp:", now)
print("Current time:", time.ctime(now))

# 6 random module
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print("Shuffled list:", lst)
print("Random sample of 3:", random.sample(lst, 3))

# 5 glob module (list py files)
print("Python files:", glob.glob("*.py"))
