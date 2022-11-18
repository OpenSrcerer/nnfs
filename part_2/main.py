from typing import Optional

import numpy as np
from numpy import around

from common.io_utils import validate_digit_input
from part_2.edalyn.accuracies.categorical import Accuracy_Categorical
from part_2.edalyn.activations.relu import Activation_ReLU
from part_2.edalyn.activations.sigmoid import Activation_Sigmoid
from part_2.edalyn.activations.softmax import Activation_Softmax
from part_2.edalyn.layers.dense import Layer_Dense
from part_2.edalyn.layers.dropout import Layer_Dropout
from part_2.edalyn.edalynmodel import EdalynModel
from part_2.edalyn.losses.cat_x_entropy import Loss_CategoricalCrossentropy
from part_2.edalyn.losses.mean_sq_error import Loss_MeanSquaredError

from part_2.edalyn.optimizers.adam import Optimizer_Adam

model: Optional[EdalynModel] = None


def run_program() -> None:
    """
    Function that serves as an entry point for the program.

    :return: None
    """
    print("""
    Hello, this is my CS340 Course Project Program (Part 1).
    Please choose from the following options:
    """, end='')

    # while True:
    #     print_choices()
    #     read_choices()
    test_model()


def read_choices() -> None:
    """
    Function that reads and maps choices to their respective functions.

    :return: None
    """
    global model  # This statement shows that we will be re-using the global scoped "table" variable

    choice = input("Your choice: ")
    if not validate_digit_input(choice, 1, 6):
        return

    if not choice == "1" and not choice == "5" and model is None:
        print("Please use choice \"1\" to initiate the model first.")
        return

    if choice == "1":
        test_model()
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        print("This program has ceased to be! It is but an ex-program!")
        quit(0)  # Exit with a happy error code :)


def test_model() -> None:
    global model

    X = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    ])

    y = np.array([
        [0, 0],
        [0, 0],
        [1, 0],
        [0, 0],
        [1, 0],
        [1, 1],
        [0, 1],
        [1, 1],
        [0, 1],
        [1, 1]
    ])

    y = np.array([
        [0, 0],
        [0, 0],
        [1, 0],
        [0, 0],
        [1, 0],
        [1, 1],
        [0, 1],
        [1, 1],
        [0, 1],
        [1, 1]
    ])

    create_model()
    model.train(X, y, batch_size=5, epochs=1000)

    a = model.predict(np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]))
    print(around(a))


def create_model():
    global model

    # >>> Create a new instance of the model
    model = EdalynModel()

    # >>> Create the model objects
    # Input layer is automatically created
    # First layer is a dropout layer to prevent over-fitting
    # layer_1_dropout = Layer_Dropout(0.1)  # 0.1 drop rate
    # av_1_relu = Activation_ReLU()

    layer_2_dense = Layer_Dense(10, 5)  # 10 inputs, 20 neurons
    av_2_relu = Activation_Sigmoid()

    layer_3_dense = Layer_Dense(5, 2)  # 20 inputs, 2 neurons
    av_3_softmax = Activation_Softmax()  # Softmax activation for final layer

    # >>> Add layers to model
    model.add_all(
        #layer_1_dropout, av_1_relu,
        layer_2_dense, av_2_relu,
        layer_3_dense, av_3_softmax
    )

    # >>> Set model attributes
    # (loss function, optimizer algorithm, accuracy function)
    model.set(loss=Loss_MeanSquaredError(), accuracy=Accuracy_Categorical(),
              optimizer=Optimizer_Adam())

    # >>> Finalize Model
    model.finalize()


run_program()