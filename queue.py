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
        self.point_next = forw
        self.point_previous = back
        self.value = value

class Queue(object):
    """Class defining a queue data structure."""

    def __init__(self):
        self.front = None
        self.back = None
        self.count = 0


    def enqueue(self, value):
        old_back = self.back
        self.back = Node(value, self.back)
        if not self.front:  #
            self.front = self.back
        else:
            old_back.point_previous = self.back
        self.count += 1


    def dequeue(self):
        try:
            val = self.front.value
            if self.front.point_previous:
                self.front = self.front.point_previous
                self.front.point_next = None
            else:
                self.front = None
            self.count -= 1

        except AttributeError:
            raise AttributeError(u"Queue is empty")
        return val

    def size(self):
        return self.count
