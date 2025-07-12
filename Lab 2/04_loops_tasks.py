# Exercise 2(ii): Loop Scenarios

# 1. List of countries
clist = ['Canada','USA','Mexico','Australia']
for country in clist:
    print(country)

# 2. Count from 0 to 100
for i in range(101):
    print(i, end=" ")
print()

# 3. Multiplication table of 5
for i in range(1, 11):
    print(f"5 x {i} = {5*i}")

# 4. Numbers 1 to 10 backwards
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# 5. Even numbers to 10
for i in range(0, 11, 2):
    print(i, end=" ")
print()

# 6. Sum from 100 to 200
total = sum(range(100, 201))
print("Sum from 100 to 200 is:", total)
