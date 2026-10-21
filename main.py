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


def selects_option(user_input, tips_library):
    """Selects the option in the menu"""
    if user_input == 1:
        add_tip(tips_library)
    elif user_input == 2:
        edit_tip()
    elif user_input == 3:
        remove_tip()
    elif user_input == 4:
        show_all_tips(tips_library)
    elif user_input == 5:
        search_tips()
    elif user_input == 6:
        sort_tips()
    elif user_input == 7:
        show_tip_total()


def press_enter():
    input("\nPress Enter to Continue to the Main Menu...\n")


def add_tip(tips_library):
    """Adds the users input for each key value pair into a dictionary then into a list"""
    date = input("\nDate: ").strip().title()
    apt = input("\nApartment: ").strip().title()
    tenant = input("\nTenant Name: ").strip().title()
    amnt = float(input("\nAmount: ").strip())
    tip_type = input("\nType: ").strip().title()
    desc = input("\nDescription: ").strip().title()

    tips = {
        "Tenant": tenant,
        "Apartment": apt,
        "Amount": amnt,
        "Type": tip_type,
        "Description": desc,
        "Date": date,
    }

    tips_library.append(tips)


def edit_tip():
    print("Editing is a work in progress...")


def remove_tip():
    print("Removing is a work in progress...")


def show_all_tips(tips_library):
    """Displays the tips list of dictionaries which include the tips information"""
    if len(tips_library) == 0:  # If no tips are in the list print this message and exit
        print("There are no tips yet.")
    else:
        for tips in (
            tips_library
        ):  # Builds the table using key value pairs from dictionary tips
            tenant = f"Tenant: {tips['Tenant']}"
            apartment = f"Apartment: {tips['Apartment']}"
            amount = f"Amount: ${tips['Amount']:.2f}"
            tip_type = f"Type: {tips['Type']}"
            description = f"Description: {tips['Description']}"
            date = f"Date: {tips['Date']}"
            row = f"| {date} | {apartment} | {tenant} | {amount} | {tip_type} | {description} |"
            print("_" * len(row))
            print(row)
            print("-" * len(row))


def search_tips():
    print("Searching is a work in progress...")


def sort_tips():
    print("Sorting is a work in progress...")


def show_tip_total():
    print("Total is a work in progress...")


def main():
    """Main while loop"""
    tips_library = []
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
        selects_option(user_input, tips_library)
        press_enter()


main()
