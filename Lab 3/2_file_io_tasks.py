# Exercise 2

# I. Store city data
n = int(input("How many cities? "))
with open("cities.txt", "w") as f:
    for _ in range(n):
        name = input("Enter city name: ")
        population = input("Enter population: ")
        mayor = input("Enter mayor: ")
        f.write(f"{name},{population},{mayor}\n")
print("City data written to cities.txt")

# II. Append message to student.txt
with open("student.txt", "a") as f:
    f.write("Now we are AI students\n")
print("Message appended to student.txt")
