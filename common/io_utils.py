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
