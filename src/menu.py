import os

from data import (
    search_year,
    sort_amount,
    sort_date,
    total_tips_math,
    transform_date,
    validate_amnt,
    validate_date,
    validate_year,
    return_tip_from_id,
    remove_tip,
    build_tip,
)


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
        remove_tip_menu(tips_jar)
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


def reinput_date():
    """Re input the date"""
    print("That input is invalid.\n\nPlease input mm-dd-yyyy with dashes in between.")
    date = input("\nDate (MM-DD-YYYY): ").strip()
    return date


def ask_whats_next(menu):
    """Asks user whats next at the end of inputs in menu"""
    response = input(
        f"\nWhats Next?\n\n1. {menu} another tip         2. Main Menu\n\n:"
    ).strip()
    while response != "1" and response != "2":
        clear_screen()
        print("\nInvalid response. Choose 1 or 2.")
        response = input(
            f"\nWhats Next?\n\n1. {menu} another tip         2. Main Menu\n\n: "
        ).strip()
    return response


def add_tip(tips_jar, tip_id):
    """Adds the users input for each key value pair into a dictionary then into a list"""
    while True:
        menu = "Add"
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
        apt = input("Apartment: ")
        spacer()
        tenant = input("Tenant Name: ")
        spacer()
        amnt = input("Amount: ").strip()
        while not validate_amnt(amnt):
            redraw_add(date, apt, tenant)
            amnt = reinput_amnt()
        redraw_add(date, apt, tenant)
        amnt = float(amnt)
        print(f"Amount: ${amnt:.2f}")
        spacer()
        tip_type = input("Tip Type(Cash, Zelle, Gift Card…): ")
        spacer()
        desc = input("Description: ")
        spacer()

        tip = build_tip(
            tip_id=tip_id,
            tenant=tenant,
            apt=apt,
            amnt=amnt,
            tip_type=tip_type,
            desc=desc,
            date=date,
        )

        tips_jar.append(tip)
        tip_id += 1
        print("\nYou have added a tip to your tip jar!")
        response = ask_whats_next(menu)
        if response == "1":
            clear_screen()
            continue
        elif response == "2":
            clear_screen()
            break
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

        if return_tip_from_id(wanted_id, tips_jar) is not None:
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
    """Menu that takes user inputs to edit the values of a tip in tips_jar"""
    if len(tips_jar) == 0:
        print("\nThere are no tips yet.")
        press_enter()
    else:
        while True:
            menu = "Edit"
            display_all_tips(tips_jar)
            print("\nInput the ID of the tip you'd like to edit\n")
            wanted_id = validate_id(tips_jar)
            reprint_all_tips(tips_jar)
            print(f"\nYou are editing tip {wanted_id}.")
            tip = return_tip_from_id(wanted_id, tips_jar)
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
                reprint_all_tips(tips_jar)
                date = input("\nDate (MM-DD-YYYY): ").strip()
                while not validate_date(date):
                    reprint_all_tips(tips_jar)
                    date = reinput_date()
                date = transform_date(date)
                tip["Date"] = date
            elif int(wanted_field) == 2:
                reprint_all_tips(tips_jar)
                tip["Apartment"] = input("\nApartment: ").strip().title()
            elif int(wanted_field) == 3:
                reprint_all_tips(tips_jar)
                tip["Tenant"] = input("\nTenant: ").strip().title()
            elif int(wanted_field) == 4:
                reprint_all_tips(tips_jar)
                amnt = input("\nAmount: ").strip()
                while not validate_amnt(amnt):
                    reprint_all_tips(tips_jar)
                    amnt = reinput_amnt()
                tip["Amount"] = float(amnt)
            elif int(wanted_field) == 5:
                reprint_all_tips(tips_jar)
                tip["Tip Type"] = (
                    input("Tip Type(Cash, Zelle, Gift Card…): ").strip().title()
                )
            elif int(wanted_field) == 6:
                reprint_all_tips(tips_jar)
                tip["Description"] = input("\nDescription: ").strip()
            reprint_all_tips(tips_jar)
            print("\nAny edits have been saved!")
            response = ask_whats_next(menu)
            if response == "1":
                clear_screen()
                continue
            elif response == "2":
                clear_screen()
                break


def remove_tip_menu(tips_jar):
    """Menu that takes user input for selecting and removing tip."""
    while True:
        menu = "Remove"
        if len(tips_jar) == 0:
            print("\nThere are no tips yet.")
            press_enter()
            break
        else:
            display_all_tips(tips_jar)
            print("\nInput the ID of the tip you'd like to remove.\n")
            wanted_id = validate_id(tips_jar)
            remove_tip(wanted_id, tips_jar)
            clear_screen()
            print("\nThe selection has been removed.\n")
            display_all_tips(tips_jar)
            response = ask_whats_next(menu)
            if response == "1":
                clear_screen()
                continue
            elif response == "2":
                clear_screen()
                break


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


def input_year():
    """Input the year to search tips"""
    year = input(
        "\nInput year you'd like to search(YYYY)\n\n(Input back to return to menu)\n\n:"
    ).strip()
    return year


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


def show_tip_total(total):
    """prints the tip total"""
    print(f"\nYour total income of tips: ${total:.2f}".title())
    press_enter()
