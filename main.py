def title_box():
    """Prints the title with box"""
    print("                   +" + "-" * 40 + "+")
    print("                   | " + "Welcome to the tip management program." + " |")
    print("                   +" + "-" * 40 + "+")


def main_menu_box():
    """Prints the menu with box"""
    menu = "| " + "Main Menu" + " |"
    print("*" * len(menu))
    print(menu)
    print("*" * len(menu))


def print_menu():
    """Function for printing main menu"""
    print("1. Add a Tip")
    print("2. Edit a tip")
    print("3. Remove a tip")
    print("4. Show all tips")
    print("5. Search tips (by year or by apartment)")
    print("6. Sort tips (by date or by amount)")
    print("7. Show total tips")
    print("8. Quit")


def selects_option(user_input):
    """Selects the option in the menu"""
    if user_input == 1:
        add_tip()
    elif user_input == 2:
        edit_tip()
    elif user_input == 3:
        remove_tip()
    elif user_input == 4:
        show_all_tips()
    elif user_input == 5:
        search_tips()
    elif user_input == 6:
        sort_tips()
    elif user_input == 7:
        show_tip_total()


def press_enter():
    input("Press Enter to Continue to the Main Menu...")


def add_tip():
    print("Adding is a work in progress...")


def edit_tip():
    print("Editing is a work in progress...")


def remove_tip():
    print("Removing is a work in progress...")


def show_all_tips():
    print("Showing all is a work in progress...")


def search_tips():
    print("Searching is a work in progress...")


def sort_tips():
    print("Sorting is a work in progress...")


def show_tip_total():
    print("Total is a work in progress...")


def main():
    """Main while loop"""
    title_box()

    while True:
        main_menu_box()
        print()
        print_menu()
        user_input = input("\nChoose your option(1 - 8): ")
        print()
        if not user_input.isdigit() or int(user_input) > 8 or int(user_input) < 1:
            print("Please enter a number between 1 and 8.\n")
            press_enter()
            continue
        user_input = int(user_input)
        if user_input == 8:
            print("Goodbye!")
            break
        selects_option(user_input)
        press_enter()


main()
