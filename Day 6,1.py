"""Tuple Operations:

Create a tuple with 5 elements.
2) Try to modify one of the elements. What happens?
Perform slicing on the tuple to extract the second and third elements.
Concatenate the tuple with another tuple."""

tuple = ("apple","banana","chikku","cherry", "strabeary")
print(tuple)
#  2 .cannot assign to function call here. Maybe you meant '==' instead of '='? to give an error

print(tuple[1:3])
new_tuple = ("60","70")
print(tuple + new_tuple)