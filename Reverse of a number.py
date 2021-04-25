# Program to find reverse of a number
num = int(input('Enter a number'))
reverse = 0
while num != 0:
    digit = num % 10
    reversed_num = reverse * 10 + digit
    num //= 10

print("Reversed Number: " + str(reverse))
