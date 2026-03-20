"""Basic Dictionary Operations:

Create a dictionary to store information about 5 cities in Karnataka and their famous dishes.
Add a new city and its dish to the dictionary.
Update the dish for Bengaluru.
Remove one city from the dictionary.
Use the keys() method to print all city names in the dictionary.
Use the values() method to print all dishes in the dictionary."""

karnataka = {
    "chikkmagaluru": "neerdosa",
    "mangalore": "korirotti",
    "udupi": "fish fry",
    "mysore": "mysore pak",
    "hasan": "mudde",
}
print("adding beluru to the list")
karnataka["beluru"] = "masal dosa"
print(karnataka)
print("updating")
karnataka["bengaluru"] ="bisi bele bath"
print(karnataka)
karnataka.pop("hasan")
print(karnataka)
print(karnataka.keys())
print(karnataka.values())