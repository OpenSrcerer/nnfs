#
# Made by Daniel Stefani for the Course Project in CS340, due December 2022.
# This work is licensed under The Unlicense, feel free to use as you wish.
# All image assets belong to their respective owners. This project is for academic purposes only.
#

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
        print(f"Invalid choice. Please enter a number from {lower_bound} to {upper_bound}.")
        return False
    return True
