""""Temperature Checker:

Write a program to check the temperature.
If the temperature is below 15°C, print 'Cold'.
If the temperature is between 15°C and 30°C, print 'Normal'.
If the temperature is above 30°C, print 'Hot'."""

tem = int(input("enter a temperature: "))
if tem < 15 :
    print("cold")
elif 15 <= tem <= 30:
    print("normal")
elif tem >=30:
    print("hot")