# Exercise 1(i): Volume of Cube
height = float(input("Enter height in cm: "))
width = float(input("Enter width in cm: "))
depth = float(input("Enter depth in cm: "))

volume = height * width * depth
print("Volume:", volume, "cm³")

if 1 <= volume <= 10:
    print("Label: Extra Small")
elif 11 <= volume <= 25:
    print("Label: Small")
elif 26 <= volume <= 75:
    print("Label: Medium")
elif 76 <= volume <= 100:
    print("Label: Large")
elif 101 <= volume <= 250:
    print("Label: Extra Large")
else:
    print("Label: Extra-Extra Large")

# Exercise 1(ii): Worker Efficiency
time = float(input("\nEnter time taken (in hours): "))
if 2 <= time < 3:
    print("Highly Efficient")
elif 3 <= time < 4:
    print("Improve speed")
elif 4 <= time <= 5:
    print("Training Required")
elif time > 5:
    print("Leave the company")
