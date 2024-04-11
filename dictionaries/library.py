class LibraryManager:
    def __init__(self):
        self.library = {}

    def add_book(self, title, author, genre, availability=True):
        if title not in self.library:
            self.library[title] = {
                "author": author,
                "genre": genre,
                "availability": availability
            }
            print(f"Book '{title}' added to the library.")
        else:
            print(f"Book '{title}' already exists in the library.")

    def borrow_book(self, title):
        if title in self.library:
            if self.library[title]["availability"]:
                self.library[title]["availability"] = False
                print(f"Book '{title}' has been borrowed.")
            else:
                print(f"Book '{title}' is currently not available.")
        else:
            print(f"Book '{title}' does not exist in the library.")

    def return_book(self, title):
        if title in self.library:
            if not self.library[title]["availability"]:
                self.library[title]["availability"] = True
                print(f"Book '{title}' has been returned.")
            else:
                print(f"Book '{title}' is already available in the library.")
        else:
            print(f"Book '{title}' does not exist in the library.")

    def search_book_by_title(self, title):
        if title in self.library:
            return self.library[title]
        else:
            print(f"Book '{title}' not found in the library.")
            return None

    def list_books(self):
        print("List of Books in the Library:")
        for title, book_info in self.library.items():
            print(f"Title: {title}, Author: {book_info['author']}, Genre: {book_info['genre']}, "
                  f"Availability: {'Available' if book_info['availability'] else 'Not Available'}")

    def list_available_books(self):
        print("List of Available Books:")
        for title, book_info in self.library.items():
            if book_info["availability"]:
                print(f"Title: {title}, Author: {book_info['author']}, Genre: {book_info['genre']}")

    def list_authors(self):
        authors = set(book_info["author"] for book_info in self.library.values())
        print("List of Authors:")
        for author in authors:
            print(author)


# Create a LibraryManager instance
library_manager = LibraryManager()

# Add some books to the library
library_manager.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
library_manager.add_book("To Kill a Mockingbird", "Harper Lee", "Fiction")
library_manager.add_book("1984", "George Orwell", "Dystopian")
library_manager.add_book("The Catcher in the Rye", "J.D. Salinger", "Coming-of-Age")

# List all books in the library
library_manager.list_books()

# Borrow a book
library_manager.borrow_book("To Kill a Mockingbird")

# List available books
library_manager.list_available_books()

# Return a book
library_manager.return_book("To Kill a Mockingbird")

# Search for a book
book_info = library_manager.search_book_by_title("1984")
if book_info:
    print("Information about '1984':", book_info)

# List all authors
library_manager.list_authors()