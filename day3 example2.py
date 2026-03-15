"""String Manipulation Exercise: Write a Python program that:
Takes a sentence as input from the user.
Prints the sentence in all uppercase and lowercase.
Replaces all spaces with underscores.
Removes leading and trailing whitespace."""

text = input("Enter text: ")
print(f'Uppercase: "{text.strip().upper()}"')
print(f'Lowercase: "{text.strip().lower()}"')
print(f'Replaced: "{text.replace(" ", "_")}"')
print(f'strip: "{text.strip()}"')