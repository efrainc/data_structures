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
        

