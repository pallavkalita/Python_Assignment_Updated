from library import add_book, register_user, borrow_book, return_book, view_books, view_user

add_book(1, "The God of Small Things", "Arundhati Roy", 3)
add_book(2, "Midnight's Children", "Salman Rushdie", 2)
add_book(3, "The White Tiger", "Aravind Adiga", 4)

register_user(101, "Rohan")
register_user(102, "Ray")

borrow_book(101, 1)
borrow_book(102, 2)
borrow_book(101, 3)

return_book(101, 1)

print("\nAll books in the library:")
view_books()

print("\nUser details:")
view_user(101)
view_user(102)
