"""Count Vowels in a String:

Write a program that counts how many vowels are in a given string using a for loop."""


string ="sushmith"
count = 0
for letter in string:
    if letter in "aeiou":
        count+=1
print("Number of vowels:",count)


