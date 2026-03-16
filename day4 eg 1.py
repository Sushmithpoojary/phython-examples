"""Logical Operator Practice: Write a Python program that takes two numbers as input from the user and checks if:
Both numbers are greater than 10 (using and).
At least one of the numbers is less than 5 (using or).
The first number is not greater than the second (using not)."""




num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
n = num1 > 10 and num2 > 10
print(n)
m = num1 < 5 or num2 < 5
print(m)
p = not(num1 > num2)
print(p)