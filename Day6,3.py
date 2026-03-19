"""Tuple and Set Comparison:

Create a list of elements and convert it into both a tuple and a set.
Print both the tuple and the set.
Try to add new elements to the tuple and set. What differences do you observe?"""\


elements = [1, 2, 3, 2, 4]

t = tuple(elements)
s = set(elements)

print("Tuple:", t)
print("Set:", s)

# Tuple (immutable)
# t.append(5)   ❌ This will give error

# Set (mutable)
s.add(5)        # ✅ Allowed
print("Updated Set:", s)