# Task 4: Count strings with same first and last characters
sample_list = ['abc', 'xyz', 'aba', '1221']
count = sum(1 for s in sample_list if len(s) >= 2 and s[0] == s[-1])
print("Expected Result:", count)