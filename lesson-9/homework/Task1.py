class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self,book):
        if len(self.borrowed_books) >=3:
            raise MemberLimitExceededException(f"Member {self.name} cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"Book {book} is already borrowed.")
        self.borrowed_books.append(book)
        book.is_borrowed = True
    
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
    
    def __str__(self):
        books = ', '.join(str(book) for book in self.borrowed_books) or "No books borrowed"
        return f"Member: {self.name}, Borrowed books: {books}"
    
class Library:
    
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, title, author):
        book = Book(title, author)
        if book not in self.books:
            self.books.append(book)
            print(f"Added {book}")
        else:
            print(f"Book {book} already exists in the library.")
    
    def add_member(self, name):
        if  not any(member.name == name for member in self.members):
            member = Member(name)
            self.members.append(member)
            print(f"Added member {name}")
        else:
            print(f"Member {name} already exists.")
    
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
            raise BookNotFoundException(f"Book {title} not found.")
    
    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        raise Exception(f"Member {name} not found.")
    
    def borrow_book(self, member_name, book_titile):
        member = self.find_member(member_name)
        book = self.find_book(book_titile)
        member.borrow_book(book)
        print(f"Book {book} borrowed by {member_name}")
    
    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        member.return_book(book)
        print(f"Book {book} returned by {member_name}")
    
if __name__ == "__main__":
    library = Library()

   
    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

    library.add_member("Alice")
    library.add_member("Bob")

    try:
        library.borrow_book("Alice", "1984")
        library.borrow_book("Alice", "To Kill a Mockingbird")
        library.borrow_book("Alice", "The Great Gatsby")
        library.borrow_book("Alice", "Nonexistent Book")
    except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
        print(e)

    try:
        library.borrow_book("Bob", "1984")  
    except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
        print(e)

    try:
        library.return_book("Alice", "1984")
        library.borrow_book("Bob", "1984")
    except Exception as e:
        print(e)

    # Displaying final status
    for member in library.members:
        print(member)

