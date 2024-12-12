class Book:
    def __init__(self, title, author, availability):
        self.__book_id = (Library().book_list[-1].__book_id + 1) if len(Library().book_list) > 0 else 1
        self.__title = title
        self.__author = author
        self.__availability = availability
    
    def borrow_book(self):
        if self.__availability == True:
            self.__availability = False
            print(f"Book '{self.__title}' borrowed successfully.")
        else:
            print("Already borrowed")
    
    def return_book(self):
        if self.__availability == False:
            self.__availability = True
            print(f"Book '{self.__title}' returned successfully.")
        else:
            print("You haven't borrowed this book!!!")


    def view_book_info(self):
        print(f"ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Avaibility: {'Available' if self.__availability else 'Not Availabe'}")
    
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
                       
------Welcome to the Library------
1. View All Books
2. Borrow Book
3. Return Book
4. Exit
                       
Enter your choice: """))

    if(choice == 1):
        book_list = Library().book_list
        print("\n\nAll books:")
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