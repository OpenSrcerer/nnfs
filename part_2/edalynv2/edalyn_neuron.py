import random

from part_2.edalynv2.edalyn_module import EdalynModule
from part_2.edalynv2.edalyn_value import EdalynValue


class EdalynNeuron(EdalynModule):
    """
    Implementation of a neuron. Contains this data:

    - Weights that connect to the previous neurons, initialized randomly.
    - A bias, initialized at 0.

    The neuron can be either linear or nonlinear. If the neuron is linear,
    the activation will be rectified using ReLU.
    """

    def __init__(self, neurons_in, not_linear=True):
        """

        Construct a new linear/nonlinear neuron with a bias of 0 and N incoming neurons.
        :param neurons_in: Number of incoming neurons.
        :param not_linear: Whether this neuron should use ReLU.
        """
        self.weights = [EdalynValue(random.uniform(-1, 1)) for _ in range(neurons_in)]
        self.bias = EdalynValue(0)
        self.not_linear = not_linear

    def __call__(self, value) -> EdalynValue:
        """
        Forward pass. Given an incoming value, computer activation.

        :param value: Incoming value.
        :return: An EdalynValue that signifies the activation of this neuron.
        """
        act = sum((wi * xi for wi, xi in zip(self.weights, value)), self.bias)
        return act.relu() if self.not_linear else act

    def __repr__(self) -> str:
        """
        :return: A string representation of this Neuron.
        """
        return f"{'ReLU' if self.not_linear else 'Linear'}Neuron({len(self.weights)})"

    def parameters(self):
        return self.weights + [self.bias]
