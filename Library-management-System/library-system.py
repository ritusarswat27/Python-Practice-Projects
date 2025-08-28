class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"{self.title} by {self.author} - {status}"


class User:
    def __init__(self, name):
        self.name = name
        self.books_issued = []

    def __str__(self):
        return f"User: {self.name}, Books Issued: {[book.title for book in self.books_issued]}"


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' added successfully.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("Books in library:")
        for book in self.books:
            print(book)

    def register_user(self, name):
        user = User(name)
        self.users.append(user)
        print(f"User '{name}' registered successfully.")

    def find_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def issue_book(self, user_name, book_title):
        user = self.find_user(user_name)
        book = self.find_book(book_title)

        if not user:
            print("User not found. Please register first.")
            return
        if not book:
            print("Book not found.")
            return
        if book.is_issued:
            print("Book is already issued.")
            return

        book.is_issued = True
        user.books_issued.append(book)
        print(f"Book '{book.title}' issued to {user.name}.")

    def return_book(self, user_name, book_title):
        user = self.find_user(user_name)
        book = self.find_book(book_title)

        if not user or book not in user.books_issued:
            print("Invalid return.")
            return

        book.is_issued = False
        user.books_issued.remove(book)
        print(f"Book '{book.title}' returned by {user.name}.")


# Driver Code

lib = Library()

while True:
        print("\n=== Library Menu ===")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Register User")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            lib.add_book(title, author)

        elif choice == '2':
            lib.display_books()

        elif choice == '3':
            name = input("Enter user name: ")
            lib.register_user(name)

        elif choice == '4':
            name = input("Enter user name: ")
            title = input("Enter book title: ")
            lib.issue_book(name, title)

        elif choice == '5':
            name = input("Enter user name: ")
            title = input("Enter book title: ")
            lib.return_book(name, title)

        elif choice == '6':
            print("Exiting Library System. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")