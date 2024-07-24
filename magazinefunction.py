from typing import Self
from magazinmodel import Magazine


def print_info(magazine):
    print(f"MAGAZINE NO:{magazine.mag_no}, Title:{magazine.title}, Format:{magazine.color_or_blackwhite_print}, Subject:{magazine.subject}, Rental Price:{magazine.rental_price}, Available Copies:{magazine.num_copies}")


class MagazineFunction:
    def __init__(self):
        self.list_of_Magazines = []
        self.__initial_data()

    def __initial_data(self):
        a_magazine1 = Magazine(mag_no="MAG_001", title="Story Books", color_or_blackwhite_print="color",
                               subject="Science", rental_price=750.00,  num_copies=10)
        a_magazine2 = Magazine(mag_no="MAG_002", title="Data Analyzing", color_or_blackwhite_print="color",
                               subject="Technology", rental_price=450.00,  num_copies=0)
        a_magazine3 = Magazine(mag_no="MAG_003", title="News", color_or_blackwhite_print="black&white",
                               subject="Sports", rental_price=550.00,  num_copies=5)

        self.list_of_Magazines.append(a_magazine1)
        self.list_of_Magazines.append(a_magazine2)
        self.list_of_Magazines.append(a_magazine3)

    def add(self):
        __mag = input("Enter Magazine Number:").upper()
        __title = input("Enter The Title:")
        #__format = input("Enter The Format:")
        while True:
            __format = input("Enter The Format (Color Print/Black & White Print): ")
            if __format not in ["Color Print", "Black & White Print"]:
                print("Invalid format. Please choose from (Color Print) or (Black & White Print).")
            else:
                break
        #__subject = input("Enter The Subject:")
        while True:
            __subject = input("Enter The Subject (Science, Technology or Sports): ")
            if __subject not in ["Science", "Technology", "Sports"]:
                print("Invalid subject. Please choose from Science, Technology, or Sports.")
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

        a_magazine = Magazine(mag_no=__mag, title=__title, color_or_blackwhite_print=__format,
                              subject=__subject, rental_price=__rental_price,  num_copies=__num_copies)
        self.list_of_Magazines.append(a_magazine)
        print(f"Successfully Added{a_magazine.mag_no}-{a_magazine.title}")

    def remove(self):
        __mag = input("Enter Magazine Number:")
        matched_data = list(
            x for x in self.list_of_Magazines if x.mag_no == __mag)
        for x in matched_data:
            self.list_of_Magazines.remove(x)
            print("Item Removed:")

    def lend(self):
        __mag = input("Enter Magazine Number:")
        __num_copies = int(input("Enter Len Copies:"))
        matched_data = list(
            x for x in self.list_of_Magazines if x.mag_no == __mag)
        for x in matched_data:
            x.num_copies -= __num_copies
            print("Magazine Lent:")

    def receive(self):
        __mag = input("Enter ISBN Number:")
        __num_copies = int(input("Enter Receive Copies:"))
        matched_data = list(
            x for x in self.list_of_Magazines if x.mag_no == __mag)
        for x in matched_data:
            x.num_copies += __num_copies
            print(f"Magazine Received With {__num_copies} Copies:")

    def display_all(self):
        for x in self.list_of_Magazines:
            print_info(magazine=x)

    def display_available(self):
        matched_data = list(
            x for x in self.list_of_Magazines if x.num_copies > 0)
        for x in matched_data:
            print_info(magazine=x)

    def display_unavailable(self):
        matched_data = list(
            x for x in self.list_of_Magazines if x.num_copies == 0)
        for x in matched_data:
            print_info(magazine=x)


