from datetime import datetime
import os

DATE_FORMAT = "%m-%d-%Y"


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
    print("5. Search tips. (by year)")
    print("6. Sort tips. (by date or by amount)")
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
        display_all_tips(tips_jar)
        press_enter()
    elif user_input == 5:
        search_tips(tips_jar)
    elif user_input == 6:
        sort_tips(tips_jar)
    elif user_input == 7:
        show_tip_total(total_tips_math(tips_jar))
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


def redraw_add(date, apt, tenant):
    """Displays the previous inputs"""
    clear_screen()
    spacer()
    print(f"Date (MM-DD-YYYY): {date}")
    spacer()
    print(f"Apartment: {apt}")
    spacer()
    print(f"Tenant Name: {tenant}")
    spacer()


def reinput_amnt():
    """Asks to reinput amount"""
    print("That input is invalid.\n\nPlease input a valid dollar amount")
    amnt = input("\nAmount: ").strip()
    return amnt


def validate_amnt(amnt):
    """Validates the amount before continuing"""
    try:
        amnt = float(amnt)
        return amnt >= 0
    except ValueError:
        return False


def reinput_date():
    """Re input the date"""
    print("That input is invalid.\n\nPlease input mm-dd-yyyy with dashes in between.")
    date = input("\nDate (MM-DD-YYYY): ").strip()
    return date


def validate_date(date):
    """Validates date is valid using datetime before continuing"""
    try:
        datetime.strptime(
            date, DATE_FORMAT
        )  # Checks if date can be turned into valid date
        return True
    except ValueError:
        return False


def transform_date(date):
    """Transforms date into correct format to store"""
    date = (datetime.strptime(date, DATE_FORMAT)).strftime(DATE_FORMAT)
    return date


def add_tip(tips_jar, tip_id):
    """Adds the users input for each key value pair into a dictionary then into a list"""
    while True:
        spacer()
        date = input("Date (MM-DD-YYYY): ").strip()
        while not validate_date(date):
            clear_screen()
            spacer()
            date = reinput_date()
        date = transform_date(date)
        clear_screen()
        spacer()
        print(f"Date (MM-DD-YYYY): {date}")
        spacer()
        apt = input("Apartment: ").strip().title()
        spacer()
        tenant = input("Tenant Name: ").strip().title()
        spacer()
        amnt = input("Amount: ").strip()
        while not validate_amnt(amnt):
            redraw_add(date, apt, tenant)
            amnt = reinput_amnt()
        redraw_add(date, apt, tenant)
        amnt = float(amnt)
        print(f"Amount: ${amnt:.2f}")
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
        print("\nYou have added a tip to your tip jar!")
        response = input(
            "\nWhats Next?\n\n1. Add another tip         2. Main Menu\n\n:"
        ).strip()
        while response != "1" and response != "2":
            clear_screen()
            print("\nInvalid response. Choose 1 or 2.")
            response = input(
                "\nWhats Next?\n\n1. Add another tip         2. Main Menu\n\n: "
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
    """Validates ID before continuing"""
    while True:
        wanted_id = input("ID: ").strip()
        while not wanted_id.isdigit():
            clear_screen()
            display_all_tips(tips_jar)
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
        display_all_tips(tips_jar)
        print("\nInput a valid ID number thats on the list.\n")
    return wanted_id


def reprint_all_tips(tips_jar):
    """Reprints table of tips"""
    clear_screen()
    display_all_tips(tips_jar)


def edit_tip(tips_jar):
    if len(tips_jar) == 0:
        print("\nThere are no tips yet.")
        press_enter()
    else:
        while True:
            display_all_tips(tips_jar)
            print("\nInput the ID of the tip you'd like to edit\n")
            wanted_id = validate_id(tips_jar)
            reprint_all_tips(tips_jar)
            print(f"\nYou are editing tip {wanted_id}.")
            print_edit_options()
            wanted_field = input("\nField to edit(1-6): ").strip()
            while not wanted_field.isdigit() or not 0 < int(wanted_field) < 7:
                clear_screen()
                reprint_all_tips(tips_jar)
                print(f"\nYou are editing tip {wanted_id}.")
                print_edit_options()
                wanted_field = input(
                    "\nInput a valid field number.\n\nField(1-6): "
                ).strip()
            if int(wanted_field) == 1:
                for tip in tips_jar:
                    if tip["ID"] == wanted_id:
                        reprint_all_tips(tips_jar)
                        date = input("\nDate (MM-DD-YYYY): ").strip()
                        while not validate_date(date):
                            reprint_all_tips(tips_jar)
                            date = reinput_date()
                        date = transform_date(date)
                        tip["Date"] = date
            elif int(wanted_field) == 2:
                for tip in tips_jar:
                    if tip["ID"] == wanted_id:
                        reprint_all_tips(tips_jar)
                        tip["Apartment"] = input("\nApartment: ").strip().title()
            elif int(wanted_field) == 3:
                for tip in tips_jar:
                    if tip["ID"] == wanted_id:
                        reprint_all_tips(tips_jar)
                        tip["Tenant"] = input("\nTenant: ").strip().title()
            elif int(wanted_field) == 4:
                for tip in tips_jar:
                    if tip["ID"] == wanted_id:
                        reprint_all_tips(tips_jar)
                        amnt = input("\nAmount: ").strip()
                        while not validate_amnt(amnt):
                            reprint_all_tips(tips_jar)
                            amnt = reinput_amnt()
                        tip["Amount"] = float(amnt)
            elif int(wanted_field) == 5:
                for tip in tips_jar:
                    if tip["ID"] == wanted_id:
                        reprint_all_tips(tips_jar)
                        tip["Tip Type"] = (
                            input("Tip Type(Cash, Zelle, Gift Card…): ").strip().title()
                        )
            elif int(wanted_field) == 6:
                for tip in tips_jar:
                    if tip["ID"] == wanted_id:
                        reprint_all_tips(tips_jar)
                        tip["Description"] = input("\nDescription: ").strip()
            reprint_all_tips(tips_jar)
            print("\nAny edits have been saved!")
            response = input(
                "\nWhats Next?\n\n1. Edit another tip         2. Main Menu\n\n:"
            ).strip()
            while response != "1" and response != "2":
                clear_screen()
                print("\nInvalid response. Choose 1 or 2.")
                response = input(
                    "\nWhats Next?\n\n1. Edit another tip         2. Main Menu\n\n: "
                ).strip()
            if response == "1":
                clear_screen()
                continue
            elif response == "2":
                clear_screen()
                break


def remove_tip(tips_jar):
    if len(tips_jar) == 0:
        print("\nThere are no tips yet.")
        press_enter()
    else:
        display_all_tips(tips_jar)
        print("\nInput the ID of the tip you'd like to remove.\n")
        wanted_id = validate_id(tips_jar)
        for i, tip in enumerate(tips_jar):
            if tip["ID"] == wanted_id:
                tips_jar.pop(i)
                break
        clear_screen()
        display_all_tips(tips_jar)
        print("\nThe selection has been removed.\n")
        press_enter()


def display_all_tips(tips_jar):
    """Displays the tips in a certain format"""
    if len(tips_jar) == 0:
        print("\nThere are no tips yet.")
        press_enter()
    else:
        print("\n_TIPS_JAR_\n")
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


# def calc_this_year():
#     current_year = datetime.now().year
#     return current_year


def input_year():
    """Input the year to search tips"""
    year = input(
        "\nInput year you'd like to search(YYYY)\n\n(Input back to return to menu)\n\n:"
    ).strip()
    return year


def validate_year(year):
    try:
        datetime.strptime(year, "%Y")
        return True
    except ValueError:
        return False


def reinput_year(on_screen):
    """Re input the year if invalid from check"""
    clear_screen()
    display_all_tips(on_screen)
    year = (
        input(
            "\nInput Valid Year.\n\nYear(YYYY):\n\n(Input back to return to menu)\n\n "
        )
        .strip()
        .lower()
    )
    return year


def search_year(year, tips_jar):
    """Search The tips by year"""
    searched_year = [tip for tip in tips_jar if tip["Date"][-4:] == year]
    return searched_year


def search_tips(tips_jar):
    """Searches and outputs tips for specified year from user"""
    if len(tips_jar) == 0:
        print("\nThere are no tips yet.")
        press_enter()
    else:
        on_screen = tips_jar
        while True:
            display_all_tips(on_screen)
            year = input_year().lower()
            while not validate_year(year) and year != "back":
                year = reinput_year(on_screen)
            if year == "back":
                clear_screen()
                break
            searched_year = search_year(year, tips_jar)
            if len(searched_year) == 0:
                clear_screen()
                display_all_tips(on_screen)
                print("\nThere are no tips under that year.")
                press_enter()
                continue
            on_screen = searched_year
            clear_screen()
            print(f"You are viewing tips from year {year}")


def user_sort_selection(tips_jar):
    """Users initial selection for how to sort the tips"""
    selection = input(
        "\n\nSort By:\n1. Highest Amount\n2. Lowest Amount\n3. Most Recent Date\n4. Furthest Date\n5. Menu\n\n"
    ).strip()
    while not selection.isdigit() or not 0 < int(selection) < 6:
        selection = reinput_sort_selection(tips_jar)
    return int(selection)


def reinput_sort_selection(on_screen):
    """Reinput user selection if input was invalid"""
    clear_screen()
    display_all_tips(on_screen)
    selection = input(
        "\nPlease input a valid option:\nSort By:\n1. Highest Amount\n2. Lowest Amount\n3. Most Recent Date\n4. Furthest Date\n5. Menu\n\n"
    ).strip()
    return selection


def return_date(tip):
    """Returns the date from the tip in date format"""
    date_text = tip["Date"]
    date = datetime.strptime(date_text, DATE_FORMAT)
    return date


def sort_date(selection, tips_jar):
    """Returns a copied sorted list by date"""
    if selection == 3:
        recent_to_furth = sorted(tips_jar, reverse=True, key=return_date)
        return recent_to_furth
    elif selection == 4:
        furth_to_recent = sorted(tips_jar, key=return_date)
        return furth_to_recent


def return_amount(tip):
    """Returns the amount value from the tip"""
    amnt = tip["Amount"]
    return amnt


def sort_amount(selection, tips_jar):
    """Sorts the amount of tips from high to low or low to high"""
    if selection == 1:
        high_to_low = sorted(tips_jar, reverse=True, key=return_amount)
        return high_to_low
    elif selection == 2:
        low_to_high = sorted(tips_jar, key=return_amount)
        return low_to_high


def sort_tips(tips_jar):
    """Sorts tips by amount or date"""
    if len(tips_jar) == 0:
        print("\nThere are no tips yet.")
        press_enter()
    else:
        display_all_tips(tips_jar)
        on_screen = tips_jar
        while True:
            selection = user_sort_selection(on_screen)
            if selection == 5:
                clear_screen()
                break
            elif selection == 1 or selection == 2:
                sorted_tips = sort_amount(selection, tips_jar)
            elif selection == 3 or selection == 4:
                sorted_tips = sort_date(selection, tips_jar)
            on_screen = sorted_tips
            clear_screen()
            display_all_tips(sorted_tips)


def total_tips_math(tips_jar):
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
