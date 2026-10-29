from datetime import datetime
import os


def title_box():
    """Prints the title with box"""
    tip_jar = "| Tip Jar |"
    print(" " * 25, "+" + ("-" * (len(tip_jar) - 2)) + "+")
    print(" " * 25, tip_jar)
    print(" " * 25, "+" + ("-" * (len(tip_jar) - 2)) + "+")


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
    print("2. Edit a tip.")
    print("3. Remove a tip.")
    print("4. Show all tips.")
    print("5. Search tips. (by year or by apartment)(Under Development)")
    print("6. Sort tips. (by date or by amount)(Under Development)")
    print("7. Show tips total amount.")
    print("8. Quit")


def selects_option(user_input, tips_jar, tip_id):
    """Selects the option in the menu"""
    clear_screen()
    if user_input == 1:
        tip_id = add_tip(tips_jar, tip_id)
    elif user_input == 2:
        edit_tip(tips_jar)
    elif user_input == 3:
        remove_tip(tips_jar)
    elif user_input == 4:
        show_all_tips(tips_jar)
        press_enter()
    elif user_input == 5:
        search_tips()
    elif user_input == 6:
        sort_tips()
    elif user_input == 7:
        show_tip_total(total_math(tips_jar))
    return tip_id


def press_enter():
    input("\nPress Enter to Continue...\n")
    clear_screen()


def clear_screen():
    """Clears the terminal when changing screens for readability depending on os"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def reinput_amnt(date, apt, tenant):
    """Shows the last inputs while asking to re input amnt"""
    clear_screen()
    spacer()
    print(f"Date (MM-DD-YYYY): {date}")
    spacer()
    print(f"Apartment: {apt}")
    spacer()
    print(f"Tenant Name: {tenant}")
    spacer()
    print("That input is invalid.\n\nPlease input a valid dollar amount")
    amnt = input("\nAmount: ").strip()
    return amnt


def validate_amnt(amnt, date, apt, tenant):
    while True:
        try:
            amnt = float(amnt)
            if amnt >= 0:
                break
            else:
                amnt = reinput_amnt(date, apt, tenant)
        except ValueError:
            amnt = reinput_amnt(date, apt, tenant)
    return amnt


def add_tip(tips_jar, tip_id):
    """Adds the users input for each key value pair into a dictionary then into a list"""
    while True:
        spacer()
        date_text = input("Date (MM-DD-YYYY): ").strip()
        while True:
            try:
                date = (datetime.strptime(date_text, "%m-%d-%Y")).strftime("%m-%d-%Y")
                clear_screen()
                spacer()
                print(f"Date (MM-DD-YYYY): {date}")
                break
            except ValueError:
                clear_screen()
                spacer()
                print(
                    "That input is invalid.\n\nPlease input mm-dd-yyyy with dashes in between."
                )
                date_text = input("\nDate (MM-DD-YYYY): ").strip()

        spacer()
        apt = input("Apartment: ").strip().title()
        spacer()
        tenant = input("Tenant Name: ").strip().title()
        spacer()
        amnt = input("Amount: ").strip()
        amnt = validate_amnt(amnt, date, apt, tenant)
        spacer()
        tip_type = input("Tip Type(Cash, Zelle, Gift Card…): ").strip().title()
        spacer()
        desc = input("Description: ").strip()
        spacer()

        tips = {
            "ID": tip_id,
            "Tenant": tenant,
            "Apartment": apt,
            "Amount": amnt,
            "Tip Type": tip_type,
            "Description": desc,
            "Date": date,
        }

        tips_jar.append(tips)
        tip_id += 1
        print("You have added a tip to your tip jar!")
        spacer()
        response = input(
            "Whats Next?\n\n1. Add another tip         2. Main Menu\n\n:"
        ).strip()
        while response != "1" and response != "2":
            clear_screen()
            print("\nInvalid response. Choose 1 or 2.")
            response = input(
                "\nWhats Next?\n\n1. Add another tip         2. Main Menu\n\n:"
            ).strip()
        if response == "1":
            clear_screen()
            continue
        elif response == "2":
            clear_screen()
            return tip_id


def print_edit_options():
    print("\n1. Date\n2. Apartment\n3. Tenant\n4. Amount\n5. Tip Type\n6. Description")


def validate_id(tips_jar):
    while True:
        wanted_id = input("ID: ").strip()
        while not wanted_id.isdigit():
            clear_screen()
            show_all_tips(tips_jar)
            wanted_id = input(
                "\nInput a valid ID number thats on the list.\n\nID: "
            ).strip()
        wanted_id = int(wanted_id)

        found = False
        for tip in tips_jar:
            if tip["ID"] == wanted_id:
                found = True
        if found:
            break
        clear_screen()
        show_all_tips(tips_jar)
        print("\nInput a valid ID number thats on the list.\n")
    return wanted_id


def edit_tip(tips_jar):
    if len(tips_jar) == 0:
        print("\nThere are no tips yet.")
        press_enter()
    else:
        show_all_tips(tips_jar)
        print("\nInput the ID of the tip you'd like to edit\n")
        wanted_id = validate_id(tips_jar)
        print_edit_options()
        wanted_field = input("\nField to edit(1-6): ").strip()
        while not wanted_field.isdigit() or not 0 < int(wanted_field) < 7:
            wanted_field = input(
                "\nInput a valid field number.\n\nField(1-6): "
            ).strip()
        if int(wanted_field) == 1:
            for tip in tips_jar:
                if tip["ID"] == wanted_id:
                    date_text = input("\nDate (MM-DD-YYYY): ").strip()
                    while True:
                        try:
                            date = (datetime.strptime(date_text, "%m-%d-%Y")).strftime(
                                "%m-%d-%Y"
                            )
                            break
                        except ValueError:
                            print(
                                "\nThat input is invalid.\n\nPlease input mm-dd-yyyy with dashes in between."
                            )
                            date_text = input("\nDate (MM-DD-YYYY): ").strip()
                    tip["Date"] = date
        elif int(wanted_field) == 2:
            for tip in tips_jar:
                if tip["ID"] == wanted_id:
                    tip["Apartment"] = input("\nApartment: ").strip().title()
        elif int(wanted_field) == 3:
            for tip in tips_jar:
                if tip["ID"] == wanted_id:
                    tip["Tenant"] = input("\nTenant: ").strip().title()
        elif int(wanted_field) == 4:
            for tip in tips_jar:
                if tip["ID"] == wanted_id:
                    tip["Amount"] = input("\nAmount: ").strip()
                    while True:
                        try:
                            tip["Amount"] = float(tip["Amount"])
                            if tip["Amount"] >= 0:
                                break
                            else:
                                print(
                                    "\nThat input is invalid.\n\nPlease input a positive dollar amount"
                                )
                                tip["Amount"] = input("\nAmount: ").strip()
                        except ValueError:
                            print(
                                "\nThat input is invalid.\n\nPlease input a valid dollar amount"
                            )
                            tip["Amount"] = input("\nAmount: ").strip()
        elif int(wanted_field) == 5:
            for tip in tips_jar:
                if tip["ID"] == wanted_id:
                    tip["Tip Type"] = (
                        input("Tip Type(Cash, Zelle, Gift Card…): ").strip().title()
                    )
        elif int(wanted_field) == 6:
            for tip in tips_jar:
                if tip["ID"] == wanted_id:
                    tip["Description"] = input("\nDescription: ").strip()
        print("\nAny edits have been saved!")
        press_enter()


def remove_tip(tips_jar):
    if len(tips_jar) == 0:
        print("\nThere are no tips yet.")
        press_enter()
    else:
        show_all_tips(tips_jar)
        print("\nInput the ID of the tip you'd like to remove.\n")
        wanted_id = validate_id(tips_jar)
        for i, tip in enumerate(tips_jar):
            if tip["ID"] == wanted_id:
                tips_jar.pop(i)
                break
        clear_screen()
        show_all_tips(tips_jar)
        print("\nThe selection has been removed.\n")
        press_enter()


def show_all_tips(tips_jar):
    """Displays the tips in a certain format"""
    if len(tips_jar) == 0:
        print("\nThere are no tips yet.")
    else:
        for tip in (
            tips_jar
        ):  # tip contains the tip information from a single dictionary each pass
            # Prints a row using key value pairs from tip.
            tip_id = f"ID: {tip['ID']}"
            tenant = f"Tenant: {tip['Tenant']}"  # assigns a variable to f string with specified label and value of key value pair in tips dictionary
            apartment = f"Apartment: {tip['Apartment']}"
            amount = f"Amount: ${tip['Amount']:.2f}"  # .2f for 2 decimal points
            tip_type = f"Tip Type: {tip['Tip Type']}"
            description = f"Description: {tip['Description']}"
            date = f"Date: {tip['Date']}"

            row = f"| {tip_id} | {date} | {apartment} | {tenant} | {amount} | {tip_type} | {description} |"

            print("_" * len(row))  # forms a line
            print(row)  # prints the variable holding the formatted f string
            print("-" * len(row))


def search_tips():
    print("Searching is a work in progress...")
    press_enter()


def sort_tips():
    print("Sorting is a work in progress...")
    press_enter()


def total_math(tips_jar):
    """Adds each value in Amount of each tip in a list and sums it up"""
    tips_total = [tip["Amount"] for tip in tips_jar]
    total = sum(tips_total)
    return total


def show_tip_total(total):
    print(f"\nYour total income of tips: ${total:.2f}".title())
    press_enter()


def main():
    """Main while loop"""

    tips_jar = []
    tip_id = 1
    clear_screen()

    while True:
        title_box()
        main_menu_box()
        print()
        print_menu()
        user_input = input("\nChoose your option(1 - 8): ").strip()
        print()
        while not user_input.isdigit() or int(user_input) > 8 or int(user_input) < 1:
            clear_screen()
            main_menu_box()
            print()
            print_menu()
            print("\nPlease enter a number between 1 and 8.")
            user_input = input("\nChoose your option(1 - 8): ").strip()
            continue
        user_input = int(user_input)
        if user_input == 8:
            print("\nGoodbye!")
            break
        tip_id = selects_option(user_input, tips_jar, tip_id)


if __name__ == "__main__":
    main()
