# Exercise 1(iii): Username & Password
username = input("Enter username: ")
password = input("Enter password: ")

if password.lower() == "abc$123":
    print("Welcome!")
else:
    print("I don't know you.")
