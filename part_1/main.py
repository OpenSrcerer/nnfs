#
# Made by Daniel Stefani for the Course Project in CS340, due December 2022.
# This work is licensed under The Unlicense, feel free to use as you wish.
# All image assets belong to their respective owners. This project is for academic purposes only.
#

import fileinput as fi
import os
from typing import Optional

from classes.table import Table
from utils.charting_utils import display_chart
from utils.io_utils import print_choices, print_order_choices, print_column_choices
from common.io_utils import validate_digit_input

# This is a global variable to contain the table.
# Reasoning for this because I don't think that global variables
# are usually good practice:
# It's easier to leave this here rather than make a Singleton.
table: Optional[Table] = None


def run_program() -> None:
    """
    Function that serves as an entry point for the program.

    :return: None
    """
    print("""
    Hello, this is my CS340 Course Project Program (Part 1).
    Please choose from the following options:
    """, end='')

    while True:
        print_choices()
        read_choices()


def read_choices() -> None:
    """
    Function that reads and maps choices to their respective functions.

    :return: None
    """
    global table  # This statement shows that we will be re-using the global scoped "table" variable

    choice = input("Your choice: ")
    if not validate_digit_input(choice, 1, 6):
        return

    if not choice == "1" and not choice == "6" and table is None:
        print("Please use choice \"1\" to load the table first.")
        return

    if choice == "1":
        load_table()
    elif choice == "2":
        search_by_laps()
    elif choice == "3":
        write_and_read_table()
    elif choice == "4":
        read_column_choices()
    elif choice == "5":
        display_chart(table)
    elif choice == "6":
        print("""
        This program has ceased to be! It is but an ex-program!
            _
          /` '\\
        /| @   l
        \\|      \\
          `\\     `\\_
            \\    __ `\\
            l  \\   `\\ `\\__
             \\  `\\./`     ``\\
               \\ ____ / \\   l
                 ||  ||  )  /
        -------(((-(((---l /-------
                        l /
                       / /
                      / /
                     //
                    /
        """)
        quit(0)  # Exit with a happy error code :)


def load_table() -> None:
    """
    Menu option 1: Reads the 6 columns of data from file partA_input_data.txt and neatly
    displays it on screen.

    :return: None
    """
    global table

    with fi.input(files=['./res/partA_input_data.csv']) as f:
        table = Table(f)
    print(table.stringify(True))


def search_by_laps() -> None:
    """
    Menu option 2: Asks the user for a limit of laps to search by, then displays only the race
    results which involve that number of home laps or greater, sorted alphabetically by Grand Prix
    name.

    :return: None
    """
    lap_choice = input("Please insert the limit of laps to search by: ")
    if not lap_choice.isdigit():
        print("Invalid choice. Please enter a numeric value.")
        return

    table.sort_by_column(0, False)
    print(table.stringify(True, lambda row: int(row[len(row) - 2]) >= int(lap_choice)))


def write_and_read_table() -> None:
    """
    Menu option 3: Calculates the average lap time per race then saves this new information as a
    7th column in file partA_output_data.txt. After saving into the file, it should also read
    back and display all 7 columns of data on the screen (the 6 original columns + the new one
    based on the calculations).

    :return: None
    """
    with open("./partA_output_data.txt", "w") as writeFile:
        writeFile.write(table.stringify(False))
        writeFile.flush()  # Flush buffer so file is immediately written
        os.fsync(writeFile)

    with open("./partA_output_data.txt", "r") as readFile:
        read_table = readFile.read()
        print(read_table)
    print("Saved partA_output_data.txt!")


def read_column_choices() -> None:
    """
    Menu option 4: Asks the user for a field to sort by, then whether the order should be
    ascending or descending. Displays on screen all data contained in the file sorted according to
    the user's instructions. This option refers to the 7-column file generated in option 3 and
    assumes it exists, otherwise the program should inform the user to execute option 3 first and
    then get back to option 4.

    :return: None
    """
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


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


run_program()
