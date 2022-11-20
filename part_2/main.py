#
# Made by Daniel Stefani for the Course Project in CS340, due December 2022.
# This work is licensed under The Unlicense, feel free to use as you wish.
# All image assets belong to their respective owners. This project is for academic purposes only.
#

import os
import re
from typing import Optional

import matplotlib.pyplot as plt

from common.io_utils import validate_digit_input
from part_2.edalynv2.edalyn_perceptron import EdalynPerceptron
from part_2.utils.io_utils import print_choices, ingest_dataset

topology = []
model: Optional[EdalynPerceptron] = None


def run_program() -> None:
    """
    Function that serves as an entry point for the program.

    :return: None
    """
    print("""
    Hello, this is my CS340 Course Project Program (Part 2).
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
    global model

    choice = input("Your choice: ")
    if not validate_digit_input(choice, 1, 5):
        return

    if not choice == "1" and not choice == "5" and model is None:
        print("Please use choice \"1\" to initiate the model first.")
        return

    if choice == "1":
        enter_topology()
    elif choice == "2":
        training_pass()
    elif choice == "3":
        classify_test_data()
    elif choice == "4":
        display_training_graphics()
    elif choice == "5":
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


def enter_topology():
    """
    Menu Option 1: Enter a new network topology to be implemented, consisting of 2-3 layers. For
    instance, if the user indicates 10-5-2 that should mean that the input layer accepts vectors
    of 10 values, the middle layer comprises 5 neurons and the output layer comprises 2
    neurons.
    """
    global model, topology

    network_choice = input("""
Please insert the topology of your network in the format:
I-h1-...-hN-O

    I = Input Layer
    H1...HN = Hidden Layers
    O = Output Layer

Topology (default 10-15-2): """)

    # Custom regex to verify topology
    if len(network_choice.strip()) == 0:
        network_choice = "10-15-2"
    if re.search("(\\d*-\\d+)+", network_choice) is None:
        print("Invalid choice. Please enter a network with a valid format.\n")
        return

    topology = list(map(lambda digit: int(digit), network_choice.split("-")))
    if len(list(filter(lambda digit: digit == "0", topology))) > 0:
        print("Invalid choice. You may not initialize a layer with 0 neurons.\n")
        return

    model = EdalynPerceptron(topology[0], topology[1:])
    print(f"Initialized a network with topology: {network_choice}")


def training_pass():
    """
    Menu Option 2: The user should be asked for a training data set file (default file name:
    training_data.txt), a learning step and a number of training epochs (hitting enter in
    any of these input questions should resort to reasonable default values). The values of the
    weights post-training should be maintained in memory, while the decreasing output of the
    cost function should be recorded in a text file named training_progress.txt (along with the
    training epoch number).
    """
    global model, topology

    # Ingest the necessary values
    datasets = ingest_dataset(topology)
    if datasets is None:  # Handle error
        return
    inputs, expected_out = datasets

    learning_rate = input("Input the learning step (default 0.05): ")
    if len(learning_rate.strip()) == 0:
        learning_rate = "0.05"

    try:
        learning_rate = float(learning_rate)
        if learning_rate <= 0:
            raise ValueError()
    except ValueError:
        print("You have entered an invalid learning rate. Please try again.")
        return

    epochs = input("Input the training epochs (default 1000): ")
    if len(epochs.strip()) == 0:
        epochs = "1000"

    try:
        epochs = int(epochs)
        if epochs < 1:
            raise ValueError()
    except ValueError:
        print("You have entered an invalid epoch number. Please try again.")
        return

    # Run training
    training_string = model.train(inputs, expected_out, learning_rate, epochs)
    with open("./training_progress.txt", "w") as writeFile:
        writeFile.write(training_string)
        writeFile.flush()  # Flush buffer so file is immediately written
        os.fsync(writeFile)
    print("Saved training_progress.txt!")


def classify_test_data():
    """
    Menu Option 3: Present the network with a series of input vectors for classification, contained in a
    comma delimited text file called input_data.txt. The network should process these vectors
    and add the corresponding output vectors at the end of each line, then save the data
    into a comma delimited text file named training_output.txt.
    """
    global model

    datasets = ingest_dataset(topology, False)
    if datasets is None:  # Handle error
        return
    inputs, _ = datasets

    outputs = model(inputs)  # Run prediction
    output_string = ""

    # Make string to write output data
    for input, output in zip(inputs, outputs):
        output_string += f"{''.join(list(map(lambda v: str(v), input)))}," \
                         f"{','.join(list(map(lambda ev: str(ev.unwrap), output)))}\n"

    with open("./training_output.txt", "w") as writeFile:
        writeFile.write(output_string)
        writeFile.flush()  # Flush buffer so file is immediately written
        os.fsync(writeFile)
    print("Saved training_output.txt!")


def display_training_graphics():
    """
    Menu Option 4: Upon conclusion of training of the ANN in part B, there should be a menu option for the
    user to select in order to have a graph displayed (in a GUI pop up window), depicting the
    gradually improving classification accuracy every 10 or every 100 training epochs or so (y
    axis: cost function output and/or success percentage and/or training error; x axis: training
    epochs). This graph should have clearly labelled axes and could be based on the same
    data which is saved into the comma delimited text file training_progress.txt.
    """
    global model

    losses = list(map(lambda v: v.unwrap, model._loss_list))
    epochs = list(((i * 100) for i, _ in enumerate(losses)))

    # Draw plot
    plt.plot(epochs, losses, "-o")
    plt.title("Loss Function vs. Epochs")
    plt.xlabel("Training Epoch")
    plt.ylabel("Loss Function Value")
    plt.yscale("log")
    plt.show()


run_program()
