from typing import List

from part_2.edalynv2.edalyn_layer import EdalynLayer
from part_2.edalynv2.edalyn_loss import EdalynMeanSquaredErrorLoss
from part_2.edalynv2.edalyn_module import EdalynModule
from part_2.edalynv2.edalyn_value import EdalynValue


class EdalynPerceptron(EdalynModule):
    """
    Implementation of a Multi Layer Perceptron using EdalynValues.
    """

    def __init__(self, input_layer, output_layers):
        """
        Create an MLP given a specific topology.
        Note that the last layer is linear (doesn't go through ReLU).

        :param input_layer: The number of neurons in the input layer.
        :param output_layers: The number of neurons in other layers ordered as an array.
        """
        sz = [input_layer] + output_layers
        self._layers = [EdalynLayer(sz[i], sz[i + 1], not_linear=i != len(output_layers) - 1)
                        for i in range(len(output_layers))]
        self._loss = EdalynMeanSquaredErrorLoss()
        self._loss_list = []

    def __call__(self, inputs) -> List[List[EdalynValue]]:
        """
        Forward pass.

        :param inputs: All inputs to the NN.
        :return: Computed outputs for the NN.
        """
        predictions = []
        for input_row in inputs:
            for layer in self._layers:
                input_row = layer(input_row)
            predictions.append(input_row)
        return predictions

    def train(self, training_data, expected_outputs, learning_rate=0.05, epochs=1000, print_every=100) -> str:
        """
        Train this network over a specific dataset.

        :param training_data: Training data that matches the input layer.
        :param expected_outputs: Expected outputs from the output layer.
        :param learning_rate: The learning rate of backprop.
        :param epochs: The training iterations that should be satisfied.
        :param print_every: Print updates in the console every N epochs.
        :return A formatted string with training progress.
        """
        output_str = ""
        for epoch in range(epochs + 1):
            # forward pass
            predicted_values = self(training_data)

            # calculate loss
            loss_value = self._loss(predicted_values, expected_outputs)

            # store loss for charting
            if epoch % 100 == 0:
                self._loss_list.append(loss_value)

            # backward pass
            self.zero_grad()  # Reset gradients
            loss_value.backward()  # Gradient descent

            # The gradient points towards maximizing loss
            # Minimize loss with -learning_rate
            for p in self.parameters():
                p.unwrap += -learning_rate * p.grad

            # Store updates in file
            if epoch % print_every == 0:
                string_to_add = f"Epoch: {epoch}/LS: {learning_rate} -> Loss: {loss_value.unwrap}\n"
                output_str += string_to_add
                print(string_to_add, end='')

        string_to_add = "------------- TRAINING COMPLETE -------------"
        output_str += string_to_add
        print(string_to_add + "\n\n")

        return output_str

    def __repr__(self):
        """
        :return: A string representation of this MLP.
        """
        return f"MLP of [{', '.join(str(layer) for layer in self._layers)}]"

    def parameters(self):
        return [p for layer in self._layers for p in layer.parameters()]
