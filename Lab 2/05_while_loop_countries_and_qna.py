# Exercise 2(iii)

# 1. Countries using while loop
clist = ["Canada", "USA", "Mexico"]
i = 0
while i < len(clist):
    print(clist[i])
    i += 1

# 2. Difference between for and while loop
print("\nFor loop is used when number of iterations is known.")
print("While loop is used when the condition is to be evaluated dynamically.")

# 3. Can you sum numbers in while loop?
total = 0
i = 1
while i <= 5:
    total += i
    i += 1
print("Sum using while loop:", total)

# 4. Can for loop be used inside while loop?
i = 0
while i < 2:
    print(f"While loop iteration {i}")
    for j in range(3):
        print("  For loop count:", j)
    i += 1
