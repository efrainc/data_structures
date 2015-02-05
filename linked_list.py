#! /usr/bin/env python
# Linked List Python file for Efrain, Mark and Henry


class Node(object):
    """Class identifying Node in linked list

    with a pointer to the next node and a value
    """

    def __init__(self, value, pointer=None):
        """Constructor for node

        which requires a value, and an optional pointer
        If no pointer is specified, it's set to None
        """
        self.pointer = pointer
        self.value = value
        return None


class Linked_list(object):
    """Class defining a linked list data structure."""

    def __init__(self):
        """Constructor for linked list

        Initializing a pointer to a head of an empty linked list.
        """
        self.head = None

    def insert(self, value):
        """Insert new node with value at the head of the list.
        """
        if not self.head:
            self.head = Node(value)
        else:
            new_node = Node(value, self.head)
            self.head = new_node

        print self.head

    def __str__(self):
        """Returns list as a Python tuple literal.
        """
        output = ""
        currentposition = self.head
        while currentposition:
            if isinstance(currentposition.value, str):
                value = "'{}'".format(currentposition.value)
                output = "{}{}".format(output, value)
            else:
                output = "{}{}".format(output, str(currentposition.value))
            currentposition = currentposition.pointer
            if currentposition:
                output += str(", ")

        output = "({})".format(output)
        return output

    def display(self):
        """Print list as a Python tuple literal.
        """
        print str(self)

    def pop(self):
        """Pop the first value off the head of the list and return value.
        """
        old_head_value = self.head.value
        self.head = self.head.pointer
        return old_head_value

    def size(self):
        """Return the length of the list.
        """
        count = 0
        currentposition = self.head
        while currentposition:
            count += 1
            currentposition = currentposition.pointer
        return count

    def search(self, value):
        """Return the node containing value in the list, if present, else None.
        """
        currentposition = self.head
        while currentposition:
            if currentposition.value == value:
                return currentposition
            currentposition = currentposition.pointer
        return None

    def remove(self, node):
        """Remove the given node from the list, assuming node is in list.
        """
        currentposition = self.head
        previousposition = None

        # for case when we are removing first node
        if currentposition == node:
            self.head = currentposition.pointer
            return None

        while currentposition:
            if currentposition == node:
                previousposition.pointer = currentposition.pointer
            previousposition = currentposition
            currentposition = currentposition.pointer
