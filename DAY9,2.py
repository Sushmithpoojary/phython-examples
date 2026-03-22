"""Odd Numbers Printer:

Create a program that prints all odd numbers between 1 and 20 using a while loop."""
 
num = 1

while num <= 20:
    if num % 2 != 0:
        print(num)
    num += 1