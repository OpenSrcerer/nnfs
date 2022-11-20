from typing import List

from part_2.edalynv2.edalyn_module import EdalynModule
from part_2.edalynv2.edalyn_neuron import EdalynNeuron
from part_2.edalynv2.edalyn_value import EdalynValue


class EdalynLayer(EdalynModule):
    """
    Implementation of a dense neural network layer.
    """

    def __init__(self, neurons_in, neurons_out, **kwargs):
        """
        Create a new layer with a N number of neurons.

        :param neurons_in: Incoming neurons.
        :param neurons_out: outgoing neurons.
        """
        self.neurons = [EdalynNeuron(neurons_in, **kwargs) for _ in range(neurons_out)]

    def __call__(self, value) -> List[EdalynValue]:
        """
        Compute the output vector of this layer.

        :param value: Incoming value.
        :return The computed outputs of the layer.
        """
        output = [neuron(value) for neuron in self.neurons]
        return output[0] if len(output) == 1 else output

    def __repr__(self) -> str:
        """
        :return: A string representation of this layer.
        """
        return f"Layer of [{', '.join(str(n) for n in self.neurons)}]"

    def parameters(self) -> List[EdalynValue]:
        return [p for n in self.neurons for p in n.parameters()]
