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
    print("""-----------------------------------------------------------------
        1) Read data from the input file & display table
        2) Search entries by given number of laps
        3) Calculate average lap time, output table to a file
        4) Sort by a specific field & display table
        5) Calculate lap time per driver, display in a pop-up window
        6) Exit the program
    -----------------------------------------------------------------
    """)


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
