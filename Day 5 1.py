"""List Manipulation Exercise:

Create a list of 5 items (strings or numbers).
Add a new item to the end of the list and another at the second position.
Remove the third item from the list.
Print the list after each operation."""

items =["apple", "banana", "cherry", "pineapple", "chikku" ]
items.append("phone")
print(items)
items.insert(1,"chips")
print(items)
items.pop(2)
print(items)