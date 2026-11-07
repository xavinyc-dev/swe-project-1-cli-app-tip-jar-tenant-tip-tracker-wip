from menu import clear_screen, main_menu_box, print_menu, selects_option, title_box


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
        user_input = input("\nChoose your option (1 - 8): ").strip()
        print()
        while not user_input.isdigit() or int(user_input) > 8 or int(user_input) < 1:
            clear_screen()
            main_menu_box()
            print()
            print_menu()
            print("\nPlease enter a number between 1 and 8.")
            user_input = input("\nChoose your option (1 - 8): ").strip()
            continue
        user_input = int(user_input)
        if user_input == 8:
            print("\nGoodbye!")
            break
        tip_id = selects_option(user_input, tips_jar, tip_id)


if __name__ == "__main__":
    main()
