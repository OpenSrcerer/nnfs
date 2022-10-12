import fileinput as fi
import os

from classes.table import Table

table: Table = None


def validate_digit_input(choice, lower_bound, upper_bound):
    if not choice.isdigit() or int(choice) < lower_bound or int(choice) > upper_bound:
        print("Invalid choice. Please enter a number from 1-7.")
        return False
    return True


def read_column_choices():
    print_column_choices()
    column_choice = input()
    if not validate_digit_input(column_choice, 1, 7):
        return

    print_order_choices()
    order_choice = input()
    if not validate_digit_input(order_choice, 1, 2):
        return

    table.sort_by_column(
        int(column_choice) - 1,
        False if order_choice == "1" else True)
    print(table.stringify(False))


def print_column_choices():
    print("""Sort by a column:
    -----------------------------------------------------------------
        1) Grand Prix Name
        2) Date of Race
        3) Race Winner
        4) Car
        5) Laps
        6) Total Time
        7) Average Lap Time
    -----------------------------------------------------------------
    """)


def print_order_choices():
    print("""Sort by this order:
    -----------------------------------------------------------------
        1) Ascending
        2) Descending
    -----------------------------------------------------------------
    """)


def read_choices():
    global table

    choice = input("Your choice: ")
    if not validate_digit_input(choice, 1, 6):
        return

    if not choice == "1" and not choice == "6" and table is None:
        print("Please use choice \"1\" to load the table first.")
        return

    if choice == "1":
        load_table()
        print(table.stringify(True))
    elif choice == "2":
        print("TODO: Not implemented yet")
    elif choice == "3":
        print("TODO: Not implemented yet")
    elif choice == "4":
        read_column_choices()
    elif choice == "5":
        print("TODO: Not implemented yet")
    elif choice == "6":
        print("This program has ceased to be! It is but an ex-program!")
        quit(0)


def print_choices():
    print("""-----------------------------------------------------------------
        1) Read data from the input file & display table
        2) Search entries by given number of laps
        3) Calculate average lap time, output table to a file
        4) Sort by a specific field & display table
        5) Calculate lap time per driver, display in a pop-up window
        6) Exit the program
    -----------------------------------------------------------------
    """)


def run_program():
    print("""
    Hello, this is my CS340 Course Project Program.
    Please choose from the following options:
    """, end='')

    while True:
        print_choices()
        read_choices()


def load_table():
    global table

    with fi.input(files=['./res/partA_input_data.csv']) as f:
        table = Table(f)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


run_program()
