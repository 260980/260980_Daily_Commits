# Write a Python program to convert a list into a nested dictionary of keys
list1 = [1, 2, 3, 4]
dict1 = curr = {}
for name in list1:
    curr[name] = {}
    curr = curr[name]
print(dict1)
