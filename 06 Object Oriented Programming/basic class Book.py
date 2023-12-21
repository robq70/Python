

class Book:
    def __init__(self, author, title ="unknown", isbn = "unknown", year = "unknown"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year

    def printData(self):
        print(self.author, self.title, self.isbn, self.year)


book1 = Book("Ola Kowalska", "Podróże", "122345XC", 2020)
book1.printData()

book2 = Book("Adam", year = 2010)
book2.printData()
