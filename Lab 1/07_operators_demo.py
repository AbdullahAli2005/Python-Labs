# Task 7: Operators Demo

# Identity
x = 6
print("x is int:", type(x) is int)
x = 7.2
print("x is not int:", type(x) is not int)

# Membership
list1 = [1,2,3,4,5]
list2 = [6,7,8,9]
for item in list1:
    if item in list2:
        print("overlapping")
        break
else:
    print("not overlapping")

# Floor division and exponent
a = 10
a //= 3
print("floor divide=", a)
a **= 5
print("exponent=", a)

# Bitwise
a = 60
b = 13
print("Line 1", a & b)
print("Line 2", a | b)
print("Line 3", a ^ b)
print("Line 4", ~a)
print("Line 5", a << 2)
print("Line 6", a >> 2)