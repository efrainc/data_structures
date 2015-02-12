#! /usr/bin/env python
# Priority Queue Python file for Efrain, Mark and Henry
import queue as q


class Pq(object):
    """Initiate priority queue"""

    def __init__(self, num=3):
        """Initiate pq with optional priority range, default is 3."""
        for x in range(1, num+1):
            setattr(self, 'que{}'.format(x), q.Queue())
        self.num_queues = num

    def insert(self, value, priority='3'):
        """Insert an item into a pq, according to priority."""
        try:
            getattr(self, 'que{}'.format(priority)).enqueue(value)
        except AttributeError:
            getattr(self, 'que{}'.format(self.num_queues)).enqueue(value)

    def pop(self):
        """Removes most important item in pq & raises error if pq is empty."""
        return self.peek_pop('pop')

    def peek(self):
        """Returns a value of the most important item, without removing it."""
        return self.peek_pop('peek')

    def peek_pop(self, pop_peek):
        for i in range(1, self.num_queues+1):
            current_q = getattr(self, 'que{}'.format(i))
            if current_q.size() > 0:
                if pop_peek == 'peek':
                    return current_q.peek()
                else:
                    return current_q.dequeue()
        raise AttributeError(u'Priority Queue is empty')
