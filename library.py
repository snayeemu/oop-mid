class Book:
    def __init__(self, book_name):
        self.book_name = book_name

class Library:
    book_list = []

    def entry_book(self, book_name):
        self.book_list.append(Book(book_name))

miu = Library()
miu.entry_book('pdf')
print(miu.book_list[0].book_name)