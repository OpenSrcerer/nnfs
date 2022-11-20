#
# Made by Daniel Stefani for the Course Project in CS340, due December 2022.
# This work is licensed under The Unlicense, feel free to use as you wish.
# All image assets belong to their respective owners. This project is for academic purposes only.
#

import fileinput as fi


def print_choices() -> None:
    """
    Function that prints the menu options.

    :return: None
    """
    print("""
-----------------------------------------------------------------
        1) Enter network topology
        2) Initiate a training pass
        3) Classify test data
        4) Display training result graphics
        5) Exit the program
-----------------------------------------------------------------
    """)


def ingest_dataset(topology, ingest_output=True) -> (list, list):
    """
    Ingest datasets.

    :param topology: Topology of network, for dataset verification.
    :param ingest_output: Whether to ingest the output dataset or not.
    :return: Tuple of datasets: (input, output).
    """
    training_file_name = "./training_data.txt" if ingest_output else "./input_data.txt"
    file_type = "training" if ingest_output else "input"

    training_file_name = input(
        f"Input the name/location of your {file_type} data file (default: {training_file_name}): ")
    if len(training_file_name.strip()) == 0:
        training_file_name = "./training_data.txt" if ingest_output else "./input_data.txt"

    # Process training file
    inputs = []
    expected_out = []
    with fi.input(files=[training_file_name]) as f:
        for i, input_output_line in enumerate(f):
            input_output_line = input_output_line.strip().split(',', 1)  # Split on first comma
            input_line = input_output_line[0]

            if len(input_line) != topology[0]:  # Invalid input data
                print(f"Invalid input data. Number of inputs does not match number of input neurons. "
                      f"{len(input_line)} != {topology[0]} (line {i + 1})")
                return
            inputs.append(list((int(char)) for char in input_line))  # Inputs

            if ingest_output:
                output_line = input_output_line[1].split(',')  # split remaining output data
                if len(output_line) != topology[-1]:  # Invalid output data
                    print(f"Invalid output data. Number of outputs does not match number of output neurons. "
                          f"{len(input_line)} != {topology[0]} (line {i + 1})")
                    return
                expected_out.append(list((int(string)) for string in output_line))  # Expected

    return inputs, expected_out
