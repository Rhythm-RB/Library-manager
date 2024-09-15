class Library:
    def __init__(self):
        self.books = []
        self.noofbooks = 0

    def addBook(self,book):
        self.books.append(book)
        self.noofbooks = len(self.books)

    def showInfo(self):
        print(f"The library has {self.noofbooks} books")
        for book in self.books:
            print(book)
            
        


l1 = Library()
l1.addBook("Harry potter1")
l1.addBook("Harry potter2")
l1.addBook("Harry potter3")

l1.showInfo()
        