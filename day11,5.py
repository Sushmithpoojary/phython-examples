"""Dictionary Comprehension:

Create a dictionary where the keys are Kannada cities, 
and the values are their populations. Use dictionary comprehension to filter out cities with populations below 10 lakhs."""
city_population={
    "chikkamagaluru":200000,
    "bangalore":10000000,
    "mangalore":26546879,
    "udupi":674636778
}
large_cities={
    city:population for city,population in city_population.items() if population >=10000000
}
print(large_cities)
