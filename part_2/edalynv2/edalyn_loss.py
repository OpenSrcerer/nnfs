from typing import List

from part_2.edalynv2.edalyn_value import EdalynValue


class EdalynLoss:
    """
    Base class that represents a loss function for an EdalynPerceptron.
    """
    def __init__(self, loss_function):
        self.loss_function = loss_function

    def __call__(self, actual_out, expected_out) -> EdalynValue:
        """
        Compute the loss function.
        
        :param actual_out: Predicted values by the MLP.
        :param expected_out: Expected output values.
        """
        return self.loss_function(actual_out, expected_out)


class EdalynMeanSquaredErrorLoss(EdalynLoss):
    """
    Implementation for MeanSquaredError loss function.
    """
    def __init__(self):
        super().__init__(mse_loss)


def mse_loss(out_pred, out_real):
    """
    :param out_pred: Predicted values by the MLP.
    :param out_real: Expected values.
    :return: Computed MSE loss value.
    """
    errors = list((subtract(out_pred_i, out_real_i) for out_pred_i, out_real_i in zip(out_pred, out_real)))
    squared_error = list(pow_2(error) for error in errors)
    sum_squared_error = sum(sum(squared_error, []))
    return sum_squared_error / len(out_real)


def pow_2(error) -> List:
    """
    :return Square every value in the given list.
    """
    return list((error_i ** 2) for error_i in error)


def subtract(out_pred_i, out_real_i):
    """
    :return A list where every element is the result of subtraction of l1[i] - l2[i].
    """
    return list((out_pred_ij - out_real_ij) for out_pred_ij, out_real_ij in zip(out_pred_i, out_real_i))