"""Set Operations:

Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.
Find the union, intersection, and difference between the two sets.
Add a new fruit to your set.
Remove a fruit from your set using both remove() and discard(). What happens when the fruit doesn’t exist?"""

s1 = {"mango", "chikku", "straberry",}
s2 = {"mango", "pineapple","watermelon"}
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
s1.add("jackfriuit")
print(s1)
s1.remove("chikku")
print(s1)
s1.discard("10")
print(s1)