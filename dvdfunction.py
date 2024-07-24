from typing import Self
from dvdmodel import Dvds


def print_info(dvd):
    print(f"DVD Number:{dvd.dvd_no}, Title:{dvd.title}, Subject:{dvd.subject}, Rental Price:{dvd.rental_price}, Available Copies:{dvd.num_copies}")


class DvdFunction:
    def __init__(self):
        self.list_of_Dvds = []
        self.__initial_data()

    def __initial_data(self):
        a_dvd1 = Dvds(dvd_no="DVD_001", title="Fundamental",
                     subject="Astronomy", rental_price=250.00,  num_copies=45)
        a_dvd2 = Dvds(dvd_no="DVD_002", title="Functions",
                     subject="Math", rental_price=450.00,  num_copies=0)
        a_dvd3 = Dvds(dvd_no="DVD_003", title="Updates",
                     subject="Technology", rental_price=550.00,  num_copies=2)

        self.list_of_Dvds.append(a_dvd1)
        self.list_of_Dvds.append(a_dvd2)
        self.list_of_Dvds.append(a_dvd3)

    def add(self):
        __dvd = input("Enter DVD Number:").upper()
        __title = input("Enter The Title:")
        #__subject = input("Enter The Subject:")
        while True:
            __subject = input("Enter The Subject (Astronomy, Math or Technology): ")
            if __subject not in ["Astronomy", "Math", "Technology"]:
                print("Invalid format. Please choose from Astronomy, Math and Technology.")
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

        a_dvd = Dvds(dvd_no=__dvd, title=__title, subject=__subject,
                    rental_price=__rental_price,  num_copies=__num_copies)
        self.list_of_Dvds.append(a_dvd)
        print(f"Successfully Added{a_dvd.dvd_no}-{a_dvd.title}")

    def remove(self):
        __dvd = input("Enter DVD Number:")
        matched_data = list(
            x for x in self.list_of_Dvds if x.dvd_no == __dvd)
        for x in matched_data:
            self.list_of_Dvds.remove(x)
            print("Item Removed:")

    def lend(self):
        __dvd = input("Enter DVD Number:")
        __num_copies = int(input("Enter Len Copies:"))
        matched_data = list(
            x for x in self.list_of_Dvds if x.dvd_no == __dvd)
        for x in matched_data:
            x.num_copies -= __num_copies
            print("DVD Lent:")

    def receive(self):
        __dvd = input("Enter DVD Number:")
        __num_copies = int(input("Enter Receive Copies:"))
        matched_data = list(
            x for x in self.list_of_Dvds if x.dvd_no == __dvd)
        for x in matched_data:
            x.num_copies += __num_copies
            print(f"DVD Received With {__num_copies} Copies:")

    def display_all(self):
        for x in self.list_of_Dvds:
            print_info(dvd=x)

    def display_available(self):
        matched_data = list(
            x for x in self.list_of_Dvds if x.num_copies > 0)
        for x in matched_data:
            print_info(dvd=x)

    def display_unavailable(self):
        matched_data = list(
            x for x in self.list_of_Dvds if x.num_copies == 0)
        for x in matched_data:
            print_info(dvd=x)



