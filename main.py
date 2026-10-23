# Separation of Concerns - each part of a program has one concern and knows as little as possible about the others
# Modularity - breaking up a program into parts
# Abstraction - the degree to which you condense something down to just a simple idea

from datetime import datetime


def title_box():
    """Prints the title with box"""
    print("                   +" + "-" * 40 + "+")
    print("                   | " + "Welcome to the tip management program." + " |")
    print("                   +" + "-" * 40 + "+")


def spacer():
    print("-" * 50)


def main_menu_box():
    """Prints the menu with box"""
    menu = "| " + "Main Menu" + " |"
    print("*" * len(menu))
    print(menu)
    print("*" * len(menu))


def print_menu():
    """Function for printing main menu"""
    print("1. Add a Tip.")
    print("2. Edit a tip.(Under Development)")
    print("3. Remove a tip.(Under Development)")
    print("4. Show all tips.")
    print("5. Search tips. (by year or by apartment)(Under Development)")
    print("6. Sort tips. (by date or by amount)(Under Development)")
    print("7. Show tips total amount.")
    print("8. Quit")


def selects_option(user_input, tips_library, tip_id):
    """Selects the option in the menu"""
    if user_input == 1:
        add_tip(tips_library, tip_id)
    elif user_input == 2:
        edit_tip()
    elif user_input == 3:
        remove_tip()
    elif user_input == 4:
        show_all_tips(tips_library)
    elif user_input == 5:
        search_tips()
    elif user_input == 6:
        sort_tips(tips_library)
    elif user_input == 7:
        show_tip_total(total_math(tips_library))


def press_enter():
    input("\nPress Enter to Continue to the Main Menu...\n")


def add_tip(tips_library, tip_id):
    """Adds the users input for each key value pair into a dictionary then into a list"""
    while True:
        spacer()
        date_text = input("\nDate (MM-DD-YYYY): ").strip()
        while True:
            try:
                date = (datetime.strptime(date_text, "%m-%d-%Y")).strftime("%m-%d-%Y")
                break
            except ValueError:
                print(
                    "\nThat input is invalid.\n\nPlease input mm-dd-yyyy with dashes in between."
                )
                date_text = input("\nDate (MM-DD-YYYY): ").strip()
        spacer()
        apt = input("\nApartment: ").strip().title()
        spacer()
        tenant = input("\nTenant Name: ").strip().title()
        spacer()
        amnt = input("\nAmount: ").strip()
        while True:
            try:
                amnt = float(amnt)
                if amnt >= 0:
                    break
                else:
                    print(
                        "\nThat input is invalid.\n\nPlease input a positive dollar amount"
                    )
                    amnt = input("\nAmount: ").strip()
            except ValueError:
                print("\nThat input is invalid.\n\nPlease input a valid dollar amount")
                amnt = input("\nAmount: ").strip()
        spacer()
        tip_type = input("\nType: ").strip().title()
        spacer()
        desc = input("\nDescription: ").strip().title()
        spacer()

        tips = {
            "ID": tip_id,
            "Tenant": tenant,
            "Apartment": apt,
            "Amount": amnt,
            "Type": tip_type,
            "Description": desc,
            "Date": date,
        }

        tips_library.append(tips)
        print("\nYou have added a tip to your tip jar!\n\nWhats Next?")
        spacer()
        response = input("\n1. Add another tip         2. Main Menu:\n").strip()
        while response != "1" and response != "2":
            print("Invalid response. Choose 1 or 2.")
            response = input("\n1. Add another tip         2. Main Menu:\n").strip()
        if response == "1":
            continue
        elif response == "2":
            break


def edit_tip():
    print("Editing is a work in progress...")


def remove_tip():
    print("Removing is a work in progress...")


def show_all_tips(tips_library):
    """Displays the tips in a certain format"""
    if len(tips_library) == 0:
        print("There are no tips yet.")
    else:
        for tip in (
            tips_library
        ):  # tip contains the tip information from a single dictionary each pass
            # Prints a row using key value pairs from tip.
            tenant = f"Tenant: {tip['Tenant']}"  # assigns a variable to f string with specified label and value of key value pair in tips dictionary
            apartment = f"Apartment: {tip['Apartment']}"
            amount = f"Amount: ${tip['Amount']:.2f}"  # .2f for 2 decimal points
            tip_type = f"Type: {tip['Type']}"
            description = f"Description: {tip['Description']}"
            date = f"Date: {tip['Date']}"

            row = f"| {date} | {apartment} | {tenant} | {amount} | {tip_type} | {description} |"

            print("_" * len(row))  # forms a line
            print(row)  # prints the variable holding the formatted f string
            print("-" * len(row))


def search_tips(tips_library):
    print("Searching is a work in progress...")


def sort_tips():
    print("Sorting is a work in progress...")


def total_math(tips_library):
    total = 0
    for tip_amount in tips_library:
        total += tip_amount["Amount"]
    return total


def show_tip_total(total):
    print(f"Your total income of tips: ${total:.2f}".title())


def main():
    """Main while loop"""
    tips_library = []
    tip_id = 1
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
        selects_option(user_input, tips_library, tip_id)
        press_enter()


main()
