class Book:
    
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available
    
    def checkout(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.title} is checked out.")
        else:
            print(f"{self.title} is not available.")
    
    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"{self.title} is returned and now available in the store.")
        else:
            print(f"{self.title} is not yet checked out.")

b = Book("Alchamist", "Paulo Coelho", "978-0062315007")

b.checkout()
b.checkout()
b.return_book()