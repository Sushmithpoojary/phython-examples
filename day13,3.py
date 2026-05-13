#Variable-Length Arguments: Write a function that accepts any number of arguments and returns their average.
def average(*numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
print(average(55,10))