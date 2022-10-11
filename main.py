import fileinput as fi
import os

from classes.table import Table

table: Table = None


def read_choices():
    choice = input("Your choice: ")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > 6:
        print("Invalid choice. Please enter a number from 1-6.")

    if choice == "1":
        load_table()
        table.sort_by_column(2, False)
        print(table)
    elif choice == "2":
        print("TODO: Not implemented yet")
    elif choice == "3":
        print("TODO: Not implemented yet")
    elif choice == "4":
        table.sort_by_column(1, False)
        print(table)
    elif choice == "5":
        print("TODO: Not implemented yet")
    elif choice == "6":
        print("TODO: Not implemented yet")


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

    print_choices()
    read_choices()


def load_table():
    global table

    with fi.input(files=['./res/partA_input_data.csv']) as f:
        table = Table(f)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


run_program()
