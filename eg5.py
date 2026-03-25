#Write a program to check whether a string is a palindrome (same forward and backward)
text = input("Enter a string: ")

# Remove spaces and convert to lowercase
clean_text = text.replace(" ", "").lower()

if clean_text == clean_text[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")