from math import ceil


class Binheap(object):
    def __init__(self):
        self.items = []


    def push(self, value):
        """Add value to bottom of binheap."""
        self.items.append(value)
        if len(self.items) > 1:
            self.sort_bottom()

    def pop(self):
        """"""


    def parent(self, position):
        if position == 0:
            raise AttributeError("At top of tree.")
        return (position-1)/2

    def child_L(self, position):
        return 2*position + 1

    def child_R(self, position):
        return 2*position + 2

    def switch(self, x, y):
        (self.items[x], self.items[y]) =(self.items[y], self.items[x])


    def sort_bottom(self):
        temp = len(self.items)-1
        while self.items[temp] > self.items[self.parent(temp)]:
            self.switch(temp, self.parent(temp))
            try:
                temp = self.parent(temp)
                self.parent(temp)
            except AttributeError:
                break

