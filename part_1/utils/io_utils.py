#
# Made by Daniel Stefani for the Course Project in CS340, due December 2022.
# This work is licensed under The Unlicense, feel free to use as you wish.
# All image assets belong to their respective owners. This project is for academic purposes only.
#

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


def print_choices() -> None:
    """
    Function that prints the menu options.

    :return: None
    """
    print("""
-----------------------------------------------------------------
        1) Read data from the input file & display table
        2) Search entries by given number of laps
        3) Calculate average lap time, output table to a file
        4) Sort by a specific field & display table
        5) Calculate lap time per driver, display in a pop-up window
        6) Exit the program
-----------------------------------------------------------------
    """)
