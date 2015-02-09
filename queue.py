#! /usr/bin/env python
# Stack Python file for Efrain, Mark and Henry

class Node(object):
    """A Node Class representing a Node in a queue.
    Each node has a pointer to the next node and a value.
    """

    def __init__(self, value, forw=None, back=None):
        """Create Node with value and optional pointer.
        If no pointer is specified, pointer is set to None.
        """
        self.point_previous = back
        self.value = value


class Queue(object):
    """Class defining a queue data structure."""

    def __init__(self):
        """Create a queue with a pointer to the front and back of an empty queue
        and set count to zero to keep track of size"""
        self.front = None
        self.back = None
        self.count = 0

    def enqueue(self, value):
        """Adds a node with the value to the back of the queue"""
        old_back = self.back
        self.back = Node(value, self.back)  # set  Nodes next to the old back
        if self.size() > 0:  # if any Nodes: set back previous to current Node
            old_back.point_previous = self.back
        else:  # adding to an empty, than define front
            self.front = self.back
        self.count += 1

    def dequeue(self):
        """Returns a value of the front node and removes it from the queue
        If the qpopulated_queueueue is empty, return AttributeError."""
        try:
            val = self.front.value
            self.front = self.front.point_previous
        except AttributeError:
            raise AttributeError(u"Queue is empty")
        self.count -= 1
        return val

    def size(self):
        """Returns the size of the queue"""
        return self.count
