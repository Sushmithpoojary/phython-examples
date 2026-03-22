"""Ticket Booking Simulation:

Write a program that simulates a bus ticket booking system. 
The bus has 8 seats.
Each time a seat is booked, the available seats decrease.
When there are no seats left, the loop stops and displays a message saying "All seats are booked."""

seats = 8

while seats > 0:
    print("Seats available:", seats)
    
    book = input("Do you want to book a seat? (yes/no): ")
    
    if book.lower() == "yes":
        seats -= 1
        print("Seat booked!\n")
    else:
        print("Booking stopped.")
        break

if seats == 0:
    print("All seats are booked.")




