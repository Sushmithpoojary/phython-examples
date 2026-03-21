"""Meal Time Checker:

Create a program that checks the time of day (24-hour format) and prints whether it's time for breakfast, lunch, or dinner.
Breakfast: 8 AM
Lunch: 1 PM
Dinner: 8 PM
If none of these times, print "It's not meal time."""


time = int(input("Enter a time in 24 hour format : "))
if time == 8:
	print("breakfast time")
elif time == 13:
	print("lunch time ")
elif time == 20:
	print("meal time")
else:
	print("It's not meal time.")

