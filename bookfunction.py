from typing import Self
from bookmodel import Book

#Available_B_Subjects = ["Science", "History", "Literature"]
def print_info(book):
    print(f"ISBN NO:{book.isbn_no}, Title:{book.title}, Format:{book.format}, Subject:{book.subject}, Rental Price:{book.rental_price}, Available Copies:{book.num_copies}")


class BookFunction:
    def __init__(self):
        self.list_of_books = []
        self.__initial_data()

    def __initial_data(self):
        a_book1 = Book(isbn_no="ISBN_0001", title="Evolution of Humans", format="Hardcover", subject="Science", rental_price=750.00,  num_copies=10)
        a_book2 = Book(isbn_no="ISBN_0002", title="AutoCAD Architecture", format="Paperblack", subject="History", rental_price=450.00,  num_copies=5)
        a_book3 = Book(isbn_no="ISBN_0003", title="Adobe PhotoShop", format="Hardcover", subject="Literature", rental_price=550.00,  num_copies=0)
        a_book4 = Book(isbn_no="ISBN_0004", title="Adobe PremirePro", format="Hardcover", subject="Literature", rental_price=550.00,  num_copies=80)
        
        self.list_of_books.append(a_book1)
        self.list_of_books.append(a_book2)
        self.list_of_books.append(a_book3)
        self.list_of_books.append(a_book4)
        

    def add(self):
        __isbn = input("Enter ISBN Number:").upper()
        __title = input("Enter The Title:")
        #__format = input("Enter The Format:")
        while True:
            __format = input("Enter The Format (Hardcover/Paperback): ")
            if __format not in ["Hardcover", "Paperback"]:
                print("Invalid format. Please choose from Hardcover of Paperback")
            else:
                break
        #__subject = input("Enter The Subject:")
        while True:
            __subject = input("Enter The Subject (Science/History/Literature): ")
            if __subject not in ["Science", "History", "Literature"]:
                print("Invalid subject. Please choose from Science, History, or Literature.")
            else:
                break
        
        try:
            __rental_price = float(input("Enter Rental Price:"))
        except ValueError:
            print("Invalid rental price. Please enter a numeric value.")
            return
        try:
            __num_copies = int(input("Enter Number of Available Copies "))
        except ValueError:
            print("Invalid number of copies. Please enter an integer value.")
            return

        a_book = Book(isbn_no=__isbn, title=__title, format=__format,
                      subject=__subject, rental_price=__rental_price,  num_copies=__num_copies)
        self.list_of_books.append(a_book)
        print(f"Successfully Added{a_book.isbn_no}-{a_book.title}")

    def remove(self):
        __isbn = input("Enter ISBN Number:")
        matched_data = list(
            x for x in self.list_of_books if x.isbn_no == __isbn)
        for x in matched_data:
            self.list_of_books.remove(x)
            print("Item Removed:")

    def lend(self):
        __isbn = input("Enter ISBN Number:")
        __num_copies = int(input("Enter Len Copies:"))
        matched_data = list(
            x for x in self.list_of_books if x.isbn_no == __isbn)
        for x in matched_data:
            x.num_copies -= __num_copies
            print("Book Lent:")

    def receive(self):
        __isbn = input("Enter ISBN Number:")
        __num_copies = int(input("Enter Receive Copies:"))
        matched_data = list(
            x for x in self.list_of_books if x.isbn_no == __isbn)
        for x in matched_data:
            x.num_copies += __num_copies
            print("Book Received With {__num_copies} Copies:")

    def display_all(self):
        for x in self.list_of_books:
            print_info(book=x)

    def display_available(self):
        matched_data = list(x for x in self.list_of_books if x.num_copies > 0)
        for x in matched_data:
            print_info(book=x)

    def display_unavailable(self):
        matched_data = list(x for x in self.list_of_books if x.num_copies == 0)
        for x in matched_data:
            print_info(book=x)


