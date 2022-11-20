from typing import List

from part_2.edalynv2.components.edalyn_layer import EdalynLayer
from part_2.edalynv2.components.edalyn_loss import EdalynMeanSquaredErrorLoss
from part_2.edalynv2.components.edalyn_module import EdalynModule
from part_2.edalynv2.components.edalyn_value import EdalynValue


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

    def __call__(self, inputs) -> List[EdalynValue]:
        """
        Forward pass.

        :param inputs: All inputs to the NN.
        :param out_real: Expected outputs of the NN.
        :return: Computed outputs for the NN.
        """
        for layer in self._layers:
            inputs = layer(inputs)
        return inputs

    def train(self, training_data, expected_outputs, learning_rate=0.05, epochs=1000, print_every=100):
        for epoch in range(epochs):
            # forward pass
            ypred = [self(x) for x in training_data]

            # calculate loss
            loss_value = self._loss(ypred, expected_outputs)

            # backward pass
            self.zero_grad()
            loss_value.backward()

            # update

            for p in self.parameters():
                p.unwrap += -learning_rate * p.grad

            if epoch % print_every == 0:
                print(epoch, loss_value.unwrap)
                print("lr", learning_rate)

        ypred = [self(x) for x in training_data]
        for out in ypred:
            print(f"{out[0].unwrap}, {out[1].unwrap}")

    def __repr__(self):
        """
        :return: A string representation of this MLP.
        """
        return f"MLP of [{', '.join(str(layer) for layer in self._layers)}]"

    def parameters(self):
        return [p for layer in self._layers for p in layer.parameters()]
