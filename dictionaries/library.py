library = {}
#TODO: function that if book is not in library adds it
def add_book(title, author, genre, availability=True):

#TODO: function that if enetred book is available sets it to False 

def borrow_book(title):
  
#TODO: function that if enetred book is not available sets it to True 

def return_book(title):
    
#TODO: function that checks if book exists in library

def search_book_by_title(title):
    
#TODO: function that lists all books in library along with author, genre and availability
def list_books():

#TODO: function that lists available books in library along with author, genre and availability
def list_available_books():

#TODO: function that lists only authors
def list_authors():
   


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
