# 7. Real-life Example: KSRTC Bus Seats Availability
'''Let’s say you want to simulate a KSRTC bus seat booking system. The bus has 5 available seats. 
Each time a seat is booked, the available seats decrease.
'''
available_seats = 5

while available_seats > 0:
    print(f"{available_seats} seats available.")
    booking = input("Do you want to book a seat? (yes/no): ").lower()
    
    if booking == "yes":
        available_seats -= 1
        print("Seat booked!")
    else:
        print("No booking made.")

print("All seats are booked!")

'''Here, the loop keeps running until all seats are booked. It checks the available seats and asks the user if they want to book one. The loop stops when there are no more seats available.
'''
# Output Example:

'''
5 seats available.
Do you want to book a seat? (yes/no): yes
Seat booked!
4 seats available.
Do you want to book a seat? (yes/no): yes
Seat booked!
...
1 seats available.
Do you want to book a seat? (yes/no): yes
Seat booked!
All seats are booked!'''