"""Nested List Challenge: Write a Python program that takes a list of lists (a 2D list) as input and:

Prints the entire matrix row by row.
Prints the sum of each row in the matrix."""
matrix=[[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    print(row)
    print("sum =", sum(row))
