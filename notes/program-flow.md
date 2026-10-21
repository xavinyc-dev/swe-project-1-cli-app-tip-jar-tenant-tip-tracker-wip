# How my Tip Tracker program works

## Start
1. The last line of the file calls `main()`, and the program starts there.
2. `main` creates an empty list called `tips_library`. Every tip gets stored in this list as a dictionary.
3. `main` calls `title_box()`, which prints the welcome box **once**, before the loop.

## The menu loop (`while True:`)
4. Each time through the loop, `main`:
   - calls `main_menu_box()` to print the "Main Menu" box,
   - prints a blank line,
   - calls `print_menu()` to print options 1–8,
   - asks the user to choose an option with `input()`. The answer is a **string**.
5. **Checking the input:** if the answer isn't a digit, or it's less than 1 or greater than 8, the program prints "Please enter a number between 1 and 8.", pauses with `press_enter()`, and then `continue` skips the rest of the loop and goes back to the top.
6. If the input passes the check, it gets converted to an **integer** with `int()`.
7. If the number is **8**, the program prints "Goodbye!" and `break` exits the loop, which ends the program.
8. Otherwise, `main` calls `selects_option(user_input, tips_library)` and passes it **the user's choice and the same list** (not a copy).

## Choosing the option (`selects_option`)
9. An `if`/`elif` chain checks the number and calls the matching function:
   - **1** → `add_tip(tips_library)`
   - **4** → `show_all_tips(tips_library)`
   - **2, 3, 5, 6, 7** → stubs that print "...is a work in progress..." for now.

## Option 1: `add_tip`
10. Asks the user for each piece of information, in this order: date, apartment, tenant name, amount, type, description.
11. Every answer is cleaned with `.strip()` (removes extra spaces at the start and end). Every answer except the amount is also run through `.title()` (capitalizes each word, so `4b` → `4B`).
12. The amount is converted with `float()` so it can have cents (`7.50`) and can be added up later.
13. The answers are put into **one dictionary** with the keys `"Tenant"`, `"Apartment"`, `"Amount"`, `"Type"`, `"Description"` and `"Date"`.
14. `.append()` adds that whole dictionary to `tips_library` as **one item**. Because `tips_library` is the same list that `main` created, the tip is still there after `add_tip` finishes.

## Option 4: `show_all_tips`
15. If the list is empty (`len(tips_library) == 0`), it prints "There are no tips yet."
16. Otherwise (`else`), a `for` loop goes through the list **one tip (dictionary) at a time**. For each tip, it:
    - gets each **value** by its key, like `tips['Amount']`,
    - adds a label to each one in an f-string, like `"Tenant: "`, and shows the amount as money with `$` and `.2f`,
    - joins them into one `row` and prints it between two lines sized with `len(row)`.

## After every option
17. Back in `main`, `press_enter()` pauses so the user can read the output.
18. When the user presses Enter, the loop goes **back to the top** (step 4) and shows the menu again. This repeats until the user picks 8.
