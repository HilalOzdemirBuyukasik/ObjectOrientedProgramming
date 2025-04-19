
#Create a Book class that represents basic information about a book.
#The class should have the following attributes: title, author, and year.
#Implement a method is_classic() that returns True if the book was published before 1970.
#Also, override the __str__() method to provide a user-friendly string representation of the book.

class Book:
    def __init__(self, title, author, year):
        self.year = int(year)
        self.author = author
        self.title = title

    def __str__(self):
        return f"'{self.title}' by {self.author}, published in {self.year}"

    def is_classic(self):
        return self.year < 1970


if __name__ == "__main__":

    book1 = Book('1984', 'George Orwell', '1949')
    book2 = Book('The midnight library', 'Matt Haig', 2020)

    print(book1)
    print('is classic?', book1.is_classic())

    print(book2)
    print('is classic?', book2.is_classic())


