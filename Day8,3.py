"""Simple Eligibility Check:

Write a program that checks whether a person is eligible for a library membership. 
If they are under 18, they get a student membership.
 If they are 60 or older, they get a senior citizen membership.
 Otherwise, they get a regular membership."""

age = int(input("enter a age: "))
if age <18:
    print("get a student membership")
elif age >= 60:
    print("get a senior citizen: ")
else:
    print("get a regular membership: ")