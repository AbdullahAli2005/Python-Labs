# Task 8: Full AI Task Example Program

# Task 1-4: Intro, Terminal, Python, Variables
print("Welcome to AI Task Demo")
x = 10
y = 5
z = x + y

# Task 5: Operators
if z == 15:
    print("z is 15")

# Task 6: Dictionary usage
student = {"name": "Ali", "id": 123}
print("Student name:", student["name"])

# Task 7: Lists and Tuples
fruits = ["apple", "banana", "cherry"]
pair = (1, 2)
print("Fruits:", fruits)
print("Pair first element:", pair[0])

# Task 8: Conditional Statements
if "banana" in fruits:
    print("Banana is available")

# Task 9: The For Loop
for fruit in fruits:
    print(fruit, "for sale")

# Task 10: User Input and While Loop
num = int(input("Enter a number to count down: "))
while num > 0:
    print(num)
    num -= 1