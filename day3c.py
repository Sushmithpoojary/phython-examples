'''Character Counter: Write a Python program that:

Asks the user for a string.
Prints how many characters are in the string, excluding spaces.'''
# Ask the user for a string
text = input("Enter a string: ")

# Remove spaces from the string
text_without_spaces = text.replace(" ", "")

# Count characters
count = len(text_without_spaces)

# Display the result
print("Number of characters (excluding spaces):", count)
