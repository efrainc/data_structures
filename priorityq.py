#! /usr/bin/env python
# Priority Queue Python file for Efrain, Mark and Henry

import queue as q


class Pq(object):
    """Initiate priority queue"""

    def __init__(self):
        """Initiate three queues with different priority"""
        self.one = q.Queue()
        self.two = q.Queue()
        self.three = q.Queue()

    def insert(self, value, priority='3'):
        if priority >= 3:
            self.three.enqueue(value)
        elif priority <= 1:
            self.one.enqueue(value)
        else:
            self.two.enqueue(value)

        # for x in range(priority):
        #     if x == priority:
        #         self.x.enqueue(value)

    def pop(self):
        if self.one.size() > 0:
            return self.one.dequeue()
        elif self.two.size() > 0:
            return self.two.dequeue()
        elif self.three.size() > 0:
            return self.three.dequeue()
        else:
            raise AttributeError(u'Priority Queue is empty')

    def peek(self):
        """Returns a value of the most important front node"""
        if self.one.size() > 0:
            return self.one.peek()
        elif self.two.size() > 0:
            return self.two.peek()
        elif self.three.size() > 0:
            return self.three.peek()
        else:
            raise AttributeError(u'Priority Queue is empty')

