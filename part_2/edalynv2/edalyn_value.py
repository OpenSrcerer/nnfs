from typing import TypeVar, Generic


T = TypeVar("T")


class EdalynValue(Generic[T]):
    """
    This is a custom "value wrapper" class created for the purposes of
    this network. It offers two main features:

    - The implementation of backpropagation, arguably the most important
    part of a neural network.

    - The storage of the gradient, indicating how changing this value
      affects the value of the parent node.
    """

    def __init__(self, value: T, _children=()):
        """
        Construct a new EdalynValue with a T value, gradient zero,
        and an empty backward closure.

        :param value: Numeric initial value for this node.
        :param _children:
        """
        self.unwrap = value
        self.grad = 0
        self._backward = lambda: None
        self._prev = set(_children)

    def __add__(self, other):
        """
        Implementation of mathematical addition, with backprop.

        :param other: Other node to perform addition with.
        :return: An EdalynValue containing the result of the addition.
        """
        other = other if isinstance(other, EdalynValue) else EdalynValue(other)  # Wrap other value if primitive
        out = EdalynValue(self.unwrap + other.unwrap, (self, other))

        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward

        return out

    def __mul__(self, other):
        """
        Implementation of mathematical multiplication, with backprop.

        :param other: Other node to perform multiplication with.
        :return: An EdalynValue containing the result of the multiplication.
        """
        other = other if isinstance(other, EdalynValue) else EdalynValue(other)
        out = EdalynValue(self.unwrap * other.unwrap, (self, other))

        def _backward():
            self.grad += other.unwrap * out.grad
            other.grad += self.unwrap * out.grad
        out._backward = _backward

        return out

    def __pow__(self, other):
        """
        Implementation of mathematical exponentiation, with backprop.

        :param other: Exponent.
        :return: An EdalynValue containing the result of the exponentiation.
        """
        assert isinstance(other, (int, float)), "int or float are the only supported types."
        out = EdalynValue(self.unwrap ** other, (self,))

        def _backward():
            self.grad += (other * self.unwrap ** (other - 1)) * out.grad
        out._backward = _backward

        return out

    def relu(self):
        """
        Rectified Linear Unit activation function implementation, with backprop.

        :return: max(0, unwrap)
        """
        out = EdalynValue(0 if self.unwrap < 0 else self.unwrap, (self,))

        def _backward():
            self.grad += (out.unwrap > 0) * out.grad
        out._backward = _backward

        return out

    def backward(self) -> None:
        """
        Perform backpropagation starting from this node. A good definition for
        backpropagation is:

        - Backpropagation is the recursive application of the derivative chain
        rule in a topological order.

        This method performs these steps:

        1. Build the topological order of the network.
        2. Run backward() for every node, therefore calculating the gradient for each.
        """
        topological_list = []
        visited_nodes = set()

        def build_topo(start_value):
            if start_value not in visited_nodes:
                visited_nodes.add(start_value)  # Visit starting node
                for child in start_value._prev:  # For every child, visit nodes
                    build_topo(child)
                topological_list.append(start_value)  # Add only when all nodes are visited
        build_topo(self)  # Build the topology with the current node as the starting node.

        self.grad = 1  # Base case: Gradient for self is always 1.0.
        for v in reversed(topological_list):
            v._backward()  # Apply the chain rule.

    def __neg__(self):
        """
        Negation implementation, expressed as multiplication by -1.

        :return An EdalynValue containing the result of the negation.
        """
        return self * -1

    def __radd__(self, other):
        """
        Special case of addition when the order of the types is reversed.

        :param other: Value to add.
        :return: An EdalynValue containing the result of the addition.
        """
        return self + other

    def __sub__(self, other):
        """
        Subtraction implementation expressed as addition with a negated value.

        :param other: Value to subtract.
        :return: An EdalynValue containing the result of the subtraction.
        """
        return self + (-other)

    def __rsub__(self, other):
        """
        Special case of subtraction when the order of the types is reversed.

        :param other: Value to subtract by.
        :return: An EdalynValue containing the result of the subtraction.
        """
        return other + (-self)

    def __rmul__(self, other):
        """
        Special case of multiplication when the order of the types is reversed.

        :param other: Value to multiply by.
        :return: An EdalynValue containing the result of the multiplication.
        """
        return self * other

    def __truediv__(self, other):
        """
        Division implementation expressed as exponentiation by -1.

        :param other: Value to division by.
        :return: An EdalynValue containing the result of the division.
        """
        return self * other**-1

    def __rtruediv__(self, other):
        """
        Special case of division when the order of the types is reversed.

        :param other: Value to divide by.
        :return: An EdalynValue containing the result of the division.
        """
        return other * self**-1

    def __repr__(self) -> str:
        """
        :return: A string representation of this EdalynValue.
        """
        return f"EdalynValue(value={self.unwrap}, grad={self.grad})"
