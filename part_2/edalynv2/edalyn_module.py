#
# Made by Daniel Stefani for the Course Project in CS340, due December 2022.
# This work is licensed under The Unlicense, feel free to use as you wish.
# All image assets belong to their respective owners. This project is for academic purposes only.
#

from typing import List

from part_2.edalynv2.edalyn_value import EdalynValue


class EdalynModule:
    """
    Wrapper class for all Edalyn type components.
    """

    def zero_grad(self) -> None:
        """
        Reset the gradient for the params of this component.
        """
        for param in self.parameters():
            param.grad = 0

    def parameters(self) -> List[EdalynValue]:
        """
        Should be overriden.

        :return: Parameters for this component.
        """
        return []
