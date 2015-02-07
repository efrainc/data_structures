#! /usr/bin/env python
# Stack Python file for Efrain, Mark and Henry

class Node(object):
    """A Node Class representing a Node in a stack.
    Each node has a pointer to the next node and a value.
    """

    def __init__(self, value, pointer=None):
        """Create Node with value and optional pointer.
        If no pointer is specified, pointer is set to None.
        """
        self.pointer = pointer
        self.value = value


class Stack(object):
    """Class defining a stack data structure."""

    def __init__(self):
        """Create a stack with a pointer to the top of an empty stack.
        """
        self.top = None

    def push(self, value):
        """Add node with value to the top of stack."""

        self.top = Node(value, self.top)

    def pop(self):
        """Unbinds top node of stack and returns its value.
        If pop() on an empty stack raises AttributeError."""
        try:
            old_top = self.top.value
            self.top = self.top.pointer
            return old_top
        except AttributeError:
            raise AttributeError(u'Cannot pop from an empty list')

    def __str__(self):
        """Returns the stack as a string representation of a Python tuple literal.
        Lists items from top to bottom.
        """
        output = ""
        currentposition = self.top
        while currentposition:
            if isinstance(currentposition.value, (str, unicode)):
                value = "'{}'".format(currentposition.value.encode('utf-8'))
                output = "{}{}".format(output, value)
            else:
                output = "{}{}".format(output, currentposition.value)
            currentposition = currentposition.pointer
            if currentposition:
                comma = ", "
                output = "{}{}".format(output, comma)
        output = "({})".format(output)
        return output
