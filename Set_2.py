# Write a Python program to convert a list of tuples into a dictionary
list1 = [('x', 1), ('x', 2), ('x', 3), ('y', 1), ('y', 2), ('y', 3), ('z', 1), ('z', 2)]
dict1 = {}
for a, b in list1:
    dict1.setdefault(a, []).append(b)
print(dict1)
