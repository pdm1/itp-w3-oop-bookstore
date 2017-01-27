class Bookstore(object):
    def __init__(self,name):
        self.name = name
        self.books = []

    def get_books(self):
        return self.books
        
    def add_book(self,book=None):
        self.books.append(book)
    
    def search_books(self,author=None, title=None):
        books = []

        for book in self.books:
            if title is None:
                if author == book.author:
                    books.append(book)
            elif author is None:
                if title.lower() in book.title.lower():
                    books.append(book)
            else:
                if author == book.author and title.lower() in book.title.lower():
                    books.append(book)
        return books
        
class Author(object):
    def __init__(self,name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []                 
        
    def get_books(self):
        return self.books               
        
class Book(object):
    def __init__(self, title, author): 
        self.title = title             
        self.author = author              
        author.books.append(self)  
