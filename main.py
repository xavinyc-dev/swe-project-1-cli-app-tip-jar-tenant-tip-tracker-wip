def print_menu():
    menu_list = [
        "1. Add a Tip",
        "2. Edit a tip",
        "3. Remove a tip",
        "4. Show all tips",
        "5. Search tips (by year or by apartment)",
        "6. Sort tips (by date or by amount)",
        "7. Show total tips",
        "8. Quit",
    ]
    while True:
        for option in menu_list:
            print(f"{option}")
        print("Welcome to the tip management program.")
        input("Choose your option(1 - 8): ")


print_menu()
