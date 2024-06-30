class Book:
    def __init__(self, title, author, pages, numwords):
        self.title = title
        self.author = author
        self.pages = pages
        self.numwords = numwords
    def get_title(self):
        return self.title
    def set_title(self, x):
        self.title = x
    def get_author(self):
        return self.author
    def set_author(self, x):
        self.author = x
    def get_pages(self):
        return self.pages
    def set_pages(self, t):
        self.pages = t
    def get_numwords(self):
        return self.numwords
    def set_numwords(self, n):
        self.numwords = n
    def reading_time(cls, numwords, pages, wordpermin = 250):
        total_word = pages * numwords
        return total_word/wordpermin

book = Book("The Planet", "John Nikolas", 23, 258)
book.set_title("The Planet")
book.set_author("John Nikolas")
book.set_pages(23)
book.set_numwords(258)

print(book.get_title())
print(book.get_author())
print(book.get_pages())
print(book.get_numwords())

class E_book(Book):
    def __init__(self, title, author, pages,numwords, format):
        Book.__init__(self, title, author, pages, numwords)
        self.format = format
    def get_format(self):
        return self.format
    def set_format(self, f):
        self.format = f
    def __str__(self):
        return (f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, "
                f"Number of Words per page: {self.numwords}, Format: {self.format}")

# Creating an instance of E_book
ebook = E_book("The Planet", "John Nikolas", str(23), str(258), "Simple")

# Printing the instance
print(ebook)
