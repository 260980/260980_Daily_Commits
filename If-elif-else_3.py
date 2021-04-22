# Write Python code that asks a user how many pizza slices they want.
slices = int(input('Enter number of slices: '))
if slices % 2 == 0:
    print("Total Price is: ", slices*120)
else:
    print("Total Price is: ", slices * 123)
