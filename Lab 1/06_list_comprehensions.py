# Task 6: List comprehensions
input_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']
lowercase_long = [x.lower() for x in input_list if len(x) > 5]
print("Lowercased (len > 5):", lowercase_long)

filtered_list = [x for i, x in enumerate(input_list) if i not in (0, 4, 5)]
print("Filtered List:", filtered_list)