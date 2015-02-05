#! /usr/bin/env python
# Stack Python file for Efrain, Mark and Henry

class Node(object):
    """Class identifying Node in stack 
    with a pointer to the next node and a value
    """

    def __init__(self, value, pointer=None):
        """Constructor for node
        which requires a value, and an optional pointer
        If no pointer is specified, it's set to None
        """
        self.pointer = pointer
        self.value = value


class Stack(object):
    """Class defining a stack data structure."""

    def __init__(self):
        """Constructor for stack
        Initializing a pointer to the top of an empty stack.
        """
        self.top = None

    def push(self, value):
        """Add node with value to the top of stack"""

        self.top = Node(value, self.top)

    def pop(self):
        """Unbindes top node of stack and retuns value
        If pop() on an empty stack raises AttributeError"""
        
        try:
            old_top = self.top.value
            self.top = self.top.pointer
            return old_top
        except AttributeError:
            raise AttributeError(u'Tried to pop an empty list')
        
    def __str__(self):
       """Returns stack as a Python tuple literal.
       List items from top to bottom.
       """
       output = ""
       currentposition = self.top
       while currentposition:
           if isinstance(currentposition.value, str):
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

