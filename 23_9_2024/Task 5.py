
bookings = {}

def add_movie(title, seats):
    bookings[title] = seats
    print(f"Added movie '{title}' with {seats} seats.")

def book_seat(title):
    if title in bookings:
        if bookings[title] > 0:
            bookings[title] -= 1
            print(f"Booked a seat for '{title}'. Seats remaining: {bookings[title]}")
        else:
            print(f"No seats available for '{title}'.")
    else:
        print(f"Movie '{title}' does not exist.")

def cancel_booking(title):
    if title in bookings:
        bookings[title] += 1
        print(f"Canceled a booking for '{title}'. Seats available: {bookings[title]}")
    else:
        print(f"Movie '{title}' does not exist.")

def check_available_seats(title):
    if title in bookings:
        return bookings[title]
    print(f"Movie '{title}' does not exist.")
    return None

# Example usage
if __name__ == "__main__":
    # Adding movies
    add_movie("Inception", 5)
    add_movie("Avatar", 10)

    # Booking seats
    book_seat("Inception")
    print(f"Available seats for 'Inception': {check_available_seats('Inception')}")

    # Booking a seat for a movie with no available seats
    for _ in range(5):
        book_seat("Inception")
    
    # Canceling a booking
    cancel_booking("Inception")
    print(f"Available seats for 'Inception' after cancellation: {check_available_seats('Inception')}")
