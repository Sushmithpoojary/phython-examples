'''String Manipulation Exercise: Write a Python program that:

Takes a sentence as input from the user.
Prints the sentence in all uppercase and lowercase.
Replaces all spaces with underscores.
Removes leading and trailing whitespace.'''
# Take sentence input from the user
sentence = input("Enter a sentence: ")

# Remove leading and trailing whitespace
trimmed_sentence = sentence.strip()

# uppercase
print("Uppercase:", trimmed_sentence.upper())

# lowercase
print("Lowercase:", trimmed_sentence.lower())

# Replace spaces with underscores
print("With underscores:", trimmed_sentence.replace(" ", "_"))

# Show the trimmed sentence
print("Trimmed sentence:", trimmed_sentence)
