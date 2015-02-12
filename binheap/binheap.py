#! /usr/bin/env python
# Queue Python file for Efrain, Mark and Henry


class Binheap(object):
    def __init__(self):
        self.items = []

    def push(self, value):
        """Add value to bottom of binheap."""
        self.items.append(value)
        if len(self.items) > 1:
            self.sort_bottom()

    def pop(self):
        """Remove top value from the binheap."""
        top = self.items[0]
        self.sort_top()
        return top

    def parent(self, position):
        """Return parent of current position."""
        if position == 0:
            raise AttributeError("At top of tree.")
        return (position-1)/2

    def child_L(self, position):
        """Return left child of current position."""
        cl = 2*position + 1
        if cl > len(self.items)-1:
            return None
        else:
            return cl

    def child_R(self, position):
        """Return right child of current position."""
        cr = 2*position + 2
        if cr > len(self.items)-1:
            return None
        else:
            return cr

    def find_max_child(self, position):
        """Return largest value between R and L child of current position."""
        ChildR = self.child_R(position)
        ChildL = self.child_L(position)
        try:
            if self.items[ChildL] >= self.items[ChildR]:
                return ChildL
            else:
                return ChildR
        except (AttributeError, IndexError, TypeError):
            if ChildL is not None:
                return ChildL
            else:
                raise TypeError

    def switch(self, x, y):
        """Switch position of two nodes"""
        (self.items[x], self.items[y]) = (self.items[y], self.items[x])

    def sort_bottom(self):
        """Bubbles up a value to the right place from bottom to top"""
        temp = len(self.items)-1
        while self.items[temp] > self.items[self.parent(temp)]:
            self.switch(temp, self.parent(temp))
            try:
                temp = self.parent(temp)
                self.parent(temp)
            except AttributeError:
                break

    def sort_top(self):
        """Pull value up from children to fill an empty position."""
        temp = 0
        while True:
            try:
                self.find_max_child(temp)
                self.switch(temp, self.find_max_child(temp))
                temp = self.find_max_child(temp)
            except TypeError:
                self.items.pop()
                break







