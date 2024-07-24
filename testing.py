"""

from bookmodel import Book

def print_details(list_of_books): #for x in books: print(f"ISBN NO:{x.isbn_no}, Title:{x.title}, Format:{x.format},
Subject:{x.subject}, Rental Price:{x.rental_price}, Available Copies:{x.num_copies}")


books = []

a_book1 = Book(isbn_no="ISBN_0001", title="Title1", format="Format1", subject="English", rental_price=350.00,
num_copies="10") a_book2 = Book(isbn_no="ISBN_0002", title="Title2", format="Format2", subject="Science",
rental_price=450.00,  num_copies="5") a_book3 = Book(isbn_no="ISBN_0003", title="Title3", format="Format3",
subject="Mathematics", rental_price=550.00,  num_copies="12") a_book4 = Book(isbn_no="ISBN_0004", title="Title4",
format="Format4", subject="JavaScript", rental_price=250.00,  num_copies="34")

books.append(a_book1)
books.append(a_book2)
books.append(a_book3)
books.append(a_book4)

print_details(books)

"""
"""
from bookfunction import BookFunction

book_fn = BookFunction()

book_fn.display_all()
book_fn.remove()
book_fn.display_available()
print("-----------------------------------------------------------------------------------------------------------")
book_fn.display_unavailable()


book_fn.receive()
book_fn.display_all()

from magazinefunction import MagazineFunction
mag_fn = MagazineFunction()


mag_fn.display_all()

from dvdfunction import DvdFunction


dvd_fn = DvdFunction()

dvd_fn.receive()
dvd_fn.display_all()"""

import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def text_animation(text):
    for i in range(len(text)):
        clear_screen()
        print(text[:i+1].center(os.get_terminal_size().columns))
        time.sleep(0.3)

text_animation("Hello, world!")










