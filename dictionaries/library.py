library = {}

def add_book(title, author, genre, availability=True):
    if title not in library:
        library[title] = {
            "author": author,
            "genre": genre,
            "availability": availability
        }
        print(f"Book '{title}' added to the library.")
    else:
        print(f"Book '{title}' already exists in the library.")

def borrow_book(title):
    if title in library:
        if library[title]["availability"]:
            library[title]["availability"] = False
            print(f"Book '{title}' has been borrowed.")
        else:
            print(f"Book '{title}' is currently not available.")
    else:
        print(f"Book '{title}' does not exist in the library.")

def return_book(title):
    if title in library:
        if not library[title]["availability"]:
            library[title]["availability"] = True
            print(f"Book '{title}' has been returned.")
        else:
            print(f"Book '{title}' is already available in the library.")
    else:
        print(f"Book '{title}' does not exist in the library.")

def search_book_by_title(title):
    if title in library:
        return library[title]
    else:
        print(f"Book '{title}' not found in the library.")
        return None

def list_books():
    print("List of Books in the Library:")
    for title, book_info in library.items():
        print(f"Title: {title}, Author: {book_info['author']}, Genre: {book_info['genre']}, "
              f"Availability: {'Available' if book_info['availability'] else 'Not Available'}")

def list_available_books():
    print("List of Available Books:")
    for title, book_info in library.items():
        if book_info["availability"]:
            print(f"Title: {title}, Author: {book_info['author']}, Genre: {book_info['genre']}")

def list_authors():
    authors = set(book_info["author"] for book_info in library.values())
    print("List of Authors:")
    for author in authors:
        print(author)


# Add some books to the library
add_book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
add_book("To Kill a Mockingbird", "Harper Lee", "Fiction")
add_book("1984", "George Orwell", "Dystopian")
add_book("The Catcher in the Rye", "J.D. Salinger", "Coming-of-Age")

# List all books in the library
list_books()

# Borrow a book
borrow_book("To Kill a Mockingbird")

# List available books
list_available_books()

# Return a book
return_book("To Kill a Mockingbird")

# Search for a book
book_info = search_book_by_title("1984")
if book_info:
    print("Information about '1984':", book_info)

# List all authors
list_authors()
