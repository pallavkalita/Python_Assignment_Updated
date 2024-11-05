

books = []
users = {}

def add_book(book_id, title, author, copies):
    books.append((book_id, title, author, copies))
    print(f"Book '{title}' added successfully.")

def register_user(user_id, user_name):
    users[user_id] = (user_name, [])
    print(f"User '{user_name}' registered successfully.")

def borrow_book(user_id, book_id):
    for book in books:
        if book[0] == book_id:
            if book[3] > 0:
                books[books.index(book)] = (book[0], book[1], book[2], book[3] - 1)
                users[user_id][1].append(book_id)
                print(f"User '{users[user_id][0]}' borrowed '{book[1]}'.")
            else:
                print("No copies available to borrow.")
            return
    print("Book not found.")

def return_book(user_id, book_id):
    if book_id in users[user_id][1]:
        for book in books:
            if book[0] == book_id:
                books[books.index(book)] = (book[0], book[1], book[2], book[3] + 1)
                users[user_id][1].remove(book_id)
                print(f"User '{users[user_id][0]}' returned '{book[1]}'.")
                return
    print("Book not found in user's borrowed list.")

def view_books():
    for book in books:
        print(f"ID: {book[0]}, Title: '{book[1]}', Author: '{book[2]}', Copies: {book[3]}")

def view_user(user_id):
    if user_id in users:
        user_name, borrowed_books = users[user_id]
        print(f"User: {user_name}, Borrowed Books: {borrowed_books}")
    else:
        print("User not found.")
