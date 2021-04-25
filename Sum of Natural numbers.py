# Program to find sum of natural numbers
num = int(input('Enter the value'))
if num < 0:
    print("Enter a positive number")
else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    print("The sum is", sum)
