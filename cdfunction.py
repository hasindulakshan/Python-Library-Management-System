from typing import Self
from cdsmodel import Compactdisk

def print_info(cd):
    print(f"CD Number:{cd.cd_no}, Title:{cd.title}, Subject:{cd.subject}, Rental Price:{cd.rental_price}, Available Copies:{cd.num_copies}")


class CdFunction:
    def __init__(self):
        self.list_of_Compactdisk = []
        self.__initial_data()

    def __initial_data(self):
        a_cd1 = Compactdisk(cd_no="CD_001", title="Hobby",
                    subject="Math", rental_price=250.00,  num_copies=45)
        a_cd2 = Compactdisk(cd_no="CD_002", title="Enjoy",
                    subject="Music", rental_price=450.00,  num_copies=0)
        a_cd3 = Compactdisk(cd_no="CD_003", title="Practice",
                    subject="Foreign Languages", rental_price=550.00,  num_copies=2)

        self.list_of_Compactdisk.append(a_cd1)
        self.list_of_Compactdisk.append(a_cd2)
        self.list_of_Compactdisk.append(a_cd3)

    def add(self):
        __cd = input("Enter CD Number:").upper()
        __title = input("Enter The Title:")
        #__subject = input("Enter The Subject:")
        while True:
            __subject = input("Enter The Subject (Music, Math or Foreign Languages): ")
            if __subject not in ["Music", "Math", "Foreign Languages"]:
                print("Invalid subject. Please choose from  Music, Math and Foreign Languages.")
            else:
                break
        try:
            __rental_price = float(input("Enter Rental Price:"))
        except ValueError:
            print("Invalid rental price. Please enter a numeric value.")
            return
        try:
            __num_copies = int(input("Enter Number of Available Copies: "))
        except ValueError:
            print("Invalid number of copies. Please enter an integer value.")
            return

        a_cd = Compactdisk(cd_no=__cd, title=__title, subject=__subject, rental_price=__rental_price,  num_copies=__num_copies)
        self.list_of_Compactdisk.append(a_cd)
        print(f"Successfully Added{a_cd.cd_no}-{a_cd.title}")

    def remove(self):
        __cd = input("Enter CD Number:")
        matched_data = list(
            x for x in self.list_of_Compactdisk if x.cd_no == __cd)
        for x in matched_data:
            self.list_of_Compactdisk.remove(x)
            print("Item Removed:")

    def lend(self):
        __cd = input("Enter CD Number:")
        __num_copies = int(input("Enter Lent Copies:"))
        matched_data = list(
            x for x in self.list_of_Compactdisk if x.cd_no == __cd)
        for x in matched_data:
            x.num_copies -= __num_copies
            print("CD Lent:")


    def receive(self):
        __cd = input("Enter CD Number:")
        __num_copies = int(input("Enter Receive Copies:"))
        matched_data = list(
            x for x in self.list_of_Compactdisk if x.cd_no == __cd)
        for x in matched_data:
            x.num_copies += __num_copies
            print(f"CD Received With {__num_copies} Copies:")

    def display_all(self):
        for x in self.list_of_Compactdisk:
            print_info(cd=x)

    def display_available(self):
        matched_data = list(
            x for x in self.list_of_Compactdisk if x.num_copies > 0)
        for x in matched_data:
            print_info(cd=x)

    def display_unavailable(self):
        matched_data = list(
            x for x in self.list_of_Compactdisk if x.num_copies == 0)
        for x in matched_data:
            print_info(cd=x)



