class Book:
    def __init__(self, title, author, availability):
        self.__book_id = (Library().book_list[-1].__book_id + 1) if len(Library().book_list) > 0 else 1
        self.__title = title
        self.__author = author
        self.__availability = availability
    
    def borrow_book(self):
        if self.__availability == True:
            self.__availability = False
        else:
            print("Already borrowed")
    
    def return_book(self):
        if self.__availability == False:
            self.__availability = True
        else:
            print("You haven't borrowed this book!!!")


    def view_book_info(self):
        print(self.__book_id, self.__title, self.__author, self.__availability)
    
    @property
    def get_book_id(self):
        return self.__book_id

class Library:
    book_list = []

    def entry_book(self, title, author, availability):
        self.book_list.append(Book(title, author, availability))





miu = Library()
miu.entry_book('My book', 'Nayeem', True)
miu.entry_book('My book', 'Nayeem', True)

while True:
    choice = int(input("""
                       
                       
Press
    1 to 'View All Books',
    2 to 'Borrow Book',
    3 to 'Return Book',
    4 to 'Exit': """))

    if(choice == 1):
        book_list = Library().book_list
        for i in range(len(book_list)):
            book_list[i].view_book_info()
    elif(choice == 2):
        book_list = Library().book_list
        book_id = int(input("Enter book_id to borrow: "))
        invalid_id = True
        for i in range(len(book_list)):
            if book_list[i].get_book_id == book_id:
                book_list[i].borrow_book()
                invalid_id = False
                break
        if invalid_id:
            print("Invalid book id!!!")
    elif(choice == 3):
        book_list = Library().book_list
        book_id = int(input("Enter book_id to return: "))
        invalid_id = True
        for i in range(len(book_list)):
            if book_list[i].get_book_id == book_id:
                book_list[i].return_book()
                invalid_id = False
                break
        if invalid_id:
            print("Invalid book id!!!")
    elif(choice == 4):
        break

# miu.book_list[1].borrow_book()
# miu.book_list[1].return_book()
# miu.book_list[1].view_book_info()