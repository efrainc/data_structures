#! /usr/bin/env python
# Queue Python file for Efrain, Mark and Henry


class Node(object):
    """A Node Class representing a Node in a queue.
    Each node has a pointer to the next node and a value.
    """

    def __init__(self, value, back=None, front=None ):
        """Create Node with value and optional pointer.
        If no pointer is specified, pointer is set to None.
        """
        self.previous = back
        self.value = value
        self.next = front


class Dll(object):
    """Class defining a dll data structure."""

    def __init__(self):
        """Create a dll with a pointer to the front and back of an empty dll
        and set count to zero to keep track of size"""
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, value):
        """Adds a node with the value to the tail of the dll"""
        old_tail = self.tail
        self.tail = Node(value, None, old_tail)
        if self.count > 0:  # if any Nodes: set tail previous to current Node
            old_tail.previous = self.tail
        else:  # adding to an empty, than define front
            self.head = self.tail
        self.count += 1

    def insert(self, value):
        """Adds a node with the value to the front of the dll"""
        old_head = self.head
        self.head = Node(value, old_head)
        if self.count > 0:  # if any Nodes: set tail previous to current Node
            old_head.next = self.head
        else:  # adding to an empty, than define front
            self.tail = self.head
        self.count += 1


    def pop(self):
        """Removes value from head of dll."""
        value = self.head.value
        try:
            if self.count > 1:
                self.head = self.head.previous
                self.head.next = None
            else:
                self.tail = None
                self.head = None
            self.count -= 1
        except AttributeError:
            AttributeError(u"DLL is empty.")
        return value


    def shift(self):
        """Removes value from tail of dll."""
        value = self.tail.value
        try:
            if self.count > 1:
                self.tail = self.tail.next
                self.tail.previous = None
            else:
                self.tail = None
                self.head = None
            self.count -= 1
        except AttributeError:
            AttributeError(u"DLL is empty.")
        return value


    def remove(self, val):
        current_node = self.head      
        while current_node:
            if current_node.value == val:
                if current_node == self.head:
                    self.pop()
                elif current_node == self.tail:
                    self.shift()
                else:
                    current_node.next.previous = current_node.previous
                    current_node.previous.next = current_node.next
                self.count -= 1
                return None
            current_node = current_node.previous
        raise AttributeError(u"Cannot find value")

    # def dequeue(self):
    #     """Returns a value of the front node and removes it from the queue
    #     If the qpopulated_queueueue is empty, return AttributeError."""
    #     try:
    #         val = self.front.value
    #         self.front = self.front.previous
    #     except AttributeError:
    #         raise AttributeError(u"Queue is empty")
    #     self.count -= 1
    #     return val

    # def size(self):
    #     """Returns the size of the queue"""
    #     return self.count
