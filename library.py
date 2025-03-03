class Book:
    def __init__(self,title,author,library):
        self.title = title 
        self.author = author 
        self.library = library 
        self.copies = []# to keep copies of a book 
        self.book_copies(self)
        
    pass

    def book_copies(self):#or i start a count to keep track        
        self.copies.append(self)        
    pass
        
    
# there can be many libraries
class Library:
    member = {}
    def __init__(self,name,member):
        self.name = name
        self.member = member 
        self.books = [] #list for a library to manage its books (instance attribute)
       #self.book = book
        

    def add_book(self,title,author,library):
        book = Book(self,title,author,library)
        self.books.append(book)

    pass
class Author:
    def __init__(self,author_name):
        self.name = author_name 
        self.books_list = []#for tracking books written by an author 
       
    pass
class Member:
    def __init__(self,name ):
        self.name = name 
        self.borrowed_books = []#when book is borrowed or returned list is updated 
    pass
        