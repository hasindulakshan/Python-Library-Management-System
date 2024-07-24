from bookfunction import BookFunction
from dvdfunction import DvdFunction
from magazinefunction import MagazineFunction
from cdfunction import CdFunction

book_func = BookFunction()
cd_func = CdFunction()
dvd_func = DvdFunction()
magazine_func = MagazineFunction()

def submenu(function_name, selected_resource):
    selected_operation = 1
    while selected_operation > 0:
        print(f"1 - Add a {selected_resource} to library")
        print(f"2 - Remove a {selected_resource} From library")
        print(f"3 - Display Available {selected_resource}s in library")
        print(f"4 - Display Unavailable {selected_resource}s in library")
        print(f"5 - Lend {selected_resource}s")
        print(f"6 - Receive {selected_resource}s")
        print("7 - Back to Main Menu")
        print("0 - Quit")
        print()
        try:
            selected_operation = int(input("Please type the number: ").strip())
            print()
        except ValueError:
            print("Invalid entry")
            continue

        if selected_operation == 1:
            function_name.add()
        elif selected_operation == 2:
            function_name.remove()
        elif selected_operation == 3:
            print()
            print(f"Available {selected_resource}s are: ")
            print("--------------------------------------------------------------------------------------------------------------------------")
            function_name.display_available()
            print("--------------------------------------------------------------------------------------------------------------------------")
        elif selected_operation == 4:
            print()
            print(f"Unavailable {selected_resource}s are: ")
            print("--------------------------------------------------------------------------------------------------------------------------")
            function_name.display_unavailable()
            print("--------------------------------------------------------------------------------------------------------------------------")
        elif selected_operation == 5:
            function_name.lend()
        elif selected_operation == 6:
            function_name.receive()
        elif selected_operation == 7:
            mainmenu()
        else:
            print("Invalid selection, Try again.")

        if 1 <= selected_operation <= 7:
            print()
            input("Press any key to continue...")

def mainmenu():
    print("*----- Main Menu -----")
    print()
    print("01 - Press 1 for Books")
    print("02 - Press 2 for Magazines")
    print("03 - Press 3 for DVD")
    print("04 - Press 4 for CD")
    print("05 - Press 5 for Exit")
    print()
    try:
        selected_resource = int(input("select your option: "))
    except ValueError:
        print("Invalid selection, Try again.")
        return

    if selected_resource == 5:
        print()
        print("==== Thank You For Using Library System ====")
        print()
        quit()
    elif selected_resource == 1:
        print()
        print("------ Welcome to Books ------")
        print()
        function_name = book_func
        submenu(function_name, "Book")
    elif selected_resource == 2:
        print()
        print("------ Welcome to Magazines ------")
        print()
        function_name = magazine_func
        submenu(function_name, "Magazine")
    elif selected_resource == 3:
        print()
        print("------ Welcome to DVDs ------")
        print()
        function_name = dvd_func
        submenu(function_name, "External DVD")
    elif selected_resource == 4:
        print()
        print("------Welcome to CDs------")
        print()
        function_name = cd_func
        submenu(function_name, "Lecture CD")
    else:
        print("Invalid selection, Try again.")
        return

while True:
    print()
    mainmenu()
