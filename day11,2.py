"""Sum of Prices:

Create a dictionary of 5 items with their prices. Write a program that calculates the total price of all items using a for loop."""
dic = {
    "phone":500,
    "watch":400,
    "shirt":300,
    "pant":200,
    "choclate":100
}
total_price=0
for price in dic.values():
    total_price += price
print(f"Total price of all time: {total_price}")



