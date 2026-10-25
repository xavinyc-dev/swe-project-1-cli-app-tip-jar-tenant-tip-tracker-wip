# TipJar - Tenant Tip Tracker (Work in Progress)

## Vision
This app is for any worker in an apartment building or hotel who has to
keep track of and organize their tips. It gives them one central place to
view and manage the tips they received: from who, where, and when. It
solves the problem of trying to manage a mix of cash and virtual tips, not knowing how much you made for the year, week or day and storing information about the tip specifically. The long-term goal is an application with a gui and database
that is easy to manage and search through data of tenant tips.

## Version 1
A terminal app for a friend of mine who works in an apartment building.
You can add, edit, and remove tips, see your total, and search and sort
your tips. Tips are stored in a list of dictionaries while the program
runs. Running it will just be python3 src/main.py until further notice.

## What each tip records
- **Tenant name** (optional, can be left blank)
- **Apartment** (for example `4B` or the floor)
- **Amount** (always a number in dollars; use `0` or an estimated value
  for physical items)
- **Type**: cash, card, gift card, physical item, or other
- **Description** (optional text, for example "bottle of wine" for a
  physical item, or details for "other")
- **Date** the tip was received, in the format `MM-DD-YYYY`
  (for example `12-24-2026`), so tips can be searched by date and yearly
  totals can be calculated
As of right now empty fields work for most of these features. All work in progress.
## Menu options (Version 1)
1. Add a tip
2. Edit a tip
3. Remove a tip
4. Show all tips
5. Search tips (by year or by apartment)
6. Sort tips (by date or by amount)
7. Show total tips
8. Quit

## How to test
1. python3 src/main.py
2. Add multiple tips, edit it, show all tips, show the total, try a bad input anywhere in the program.
  
## Version 1.5
- Save tips to a JSON file so they're still there the next time the
  program runs

## Not in Version 1
- A real database (SQL)
- Searching by exact date or date range
- Year-to-year comparison
- A visual interface
- Access from other devices

## Design
Each operation (add, remove, edit, search, sort, total) lives in its own
function. The menu only calls those functions, so switching to a real
database later only means rewriting the insides of those functions.
