import fileinput as fi
import os
from typing import Optional

from classes.table import Table

# This is a global variable to contain the table.
# Reasoning for this because I don't think that global variables
# are usually good practice:
# It's easier to leave this here rather than make a Singleton.
table: Optional[Table] = None


def write_and_read_table() -> None:
    """
    Menu option 3: Calculates the average lap time per race then saves this new information as a
    7th column in file partA_output_data.tx t . After saving into the file, it should also read
    back and display all 7 columns of data on the screen (the 6 original columns + the new one
    based on the calculations).

    :return: None
    """
    with open("partA_output_data.txt", "w") as writeFile:
        writeFile.write(table.stringify(False))
        writeFile.flush()  # Flush buffer so file is immediately written
        os.fsync(writeFile)

    with open("partA_output_data.txt", "r") as readFile:
        read_table = readFile.read()
        print(read_table)


def validate_digit_input(choice, lower_bound, upper_bound) -> bool:
    """
    Utility function to validate that a string satisfies these conditions:

    1. The string is a digit
    2. The string is lesser than the upper bound
    3. The string is greater than the lower bound

    :param choice: String to validate based on the aforementioned conditions.
    :param lower_bound: Lower bound for string validation.
    :param upper_bound: Upper bound for string validation.
    :return: Whether the given string passes the aforementioned criteria.
    """
    if not choice.isdigit() or int(choice) < lower_bound or int(choice) > upper_bound:
        print("Invalid choice. Please enter a number from 1-7.")
        return False
    return True


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
    print(table.stringify(False, lambda row: int(row[len(row) - 3]) >= int(lap_choice)))


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


def print_column_choices() -> None:
    """
    Utility function that prints the available column choices.

    :return: None
    """
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


def print_order_choices() -> None:
    """
    Utility function that prints the available order choices.

    :return: None
    """
    print("""Sort by this order:
    -----------------------------------------------------------------
        1) Ascending
        2) Descending
    -----------------------------------------------------------------
    """)


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
        print("TODO: Not implemented yet")
    elif choice == "6":
        print("This program has ceased to be! It is but an ex-program!")
        quit(0)  # Exit with a happy error code :)


def print_choices() -> None:
    """
    Function that prints the menu options.

    :return: None
    """
    print("""-----------------------------------------------------------------
        1) Read data from the input file & display table
        2) Search entries by given number of laps
        3) Calculate average lap time, output table to a file
        4) Sort by a specific field & display table
        5) Calculate lap time per driver, display in a pop-up window
        6) Exit the program
    -----------------------------------------------------------------
    """)


def run_program() -> None:
    """
    Function that serves as an entry point for the program.

    :return:
    """
    print("""
    Hello, this is my CS340 Course Project Program.
    Please choose from the following options:
    """, end='')

    while True:
        print_choices()
        read_choices()


def load_table() -> None:
    """
    Menu option 1: Reads the 6 columns of data from file partA_input_data.tx t and neatly
    displays it on screen.

    :return: None
    """
    global table

    with fi.input(files=['./res/partA_input_data.csv']) as f:
        table = Table(f)
    print(table.stringify(True))


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

run_program()
