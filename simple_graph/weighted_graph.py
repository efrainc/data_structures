#! /usr/bin/env python

# Simple Graph project for Efrain, Henry, Mark
# Graph is unweighted but directed

import time
from collections import OrderedDict


def timed_func(func):
    """Decorator for timing our traversal methods."""
    def timed(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print "time expired: %s" % elapsed
        return result
    return timed


class Wgraph(object):
    """A class defining a unweighted direct simple graph."""

    def __init__(self):
        """Instantiates simple graph"""
        self.dict = {}

    def nodes(self):
        """return list of all nodes in a graph"""
        return self.dict.keys()

    def edges(self):
        """return a list of all edges in the graph"""
        return [(k, val) for k, v in self.dict.iteritems() for val in v]

    def add_node(self, node):
        """adds a new node 'n' to the graph. Nodes must be hashable values."""
        try:
            self.dict.setdefault(node, OrderedDict())
        except (AttributeError, TypeError):
            raise "Node Value must be hashable value"

    def has_node(self, n):
        """True if node 'n' is contained in the graph, False if not."""
        return n in self.dict

    def add_edge(self, n1, n2, weight=0):
        """Adds a new edge to the graph connecting 'n1' to 'n2', if either n1
        or n2 are not already present in the graph, they should be added."""
        self.add_node(n1)
        self.add_node(n2)
        self.dict[n1][n2] = weight

    def del_node(self, n):
        """Delete 'n' from the graph, raise error if node doesn't exist."""
        try:
            del self.dict[n]
            # remove edges pointing to n
            for key, value in self.dict.iteritems():
                if n in value:
                    del self.dict[key][n]
        except (ValueError, KeyError):
                raise AttributeError('No Such Node Exists')

    def del_edge(self, n1, n2):
        """Delete edge connecting 'n1' and 'n2' from the graph, raise
        error if edge doesn't exist."""
        try:
            del self.dict[n1][n2]
        except (ValueError, KeyError):
            raise AttributeError('No Such Edge Exists')

    def neighbors(self, n):
        """Returns the list of all nodes with edges leading to them from n,
        raise error if n is not in g."""

        try:
            return self.dict[n].keys()
        except KeyError:
            raise KeyError('Node not in graph.')

    def adjacent(self, n1, n2):
        """returns True if there is an edge connecting n1 and n2, False if not,
        raises an error if either of the supplied nodes are not in g."""
        try:
            return n2 in self.dict[n1]
        except KeyError:
            raise KeyError('Node(s) not in graph.')

    @timed_func
    def depth_first_traversal(self, start):
        """Perform a full depth-first traversal of the graph beginning at start.
        Return the path when complete."""
        return self.recursive_dft(start, [])


    def recursive_dft(self, start, visited=[]):
        """Recursive function for depth first traversal."""
        if start not in visited:
            visited.append(start)
            for i in self.neighbors(start):
                self.recursive_dft(i, visited)
            return visited

    @timed_func
    def breadth_first_traversal(self, start):
        """Perform a full breadth-first traversal of the graph beginning at start.
        Return the path when complete."""
        visited = []
        visited.append(start)
        start_visited = visited
        while True:
            temp = []
            for node_ in start_visited:
                for i in self.neighbors(node_):
                    if i not in visited:
                        visited.append(i)
                        temp.append(i)
            start_visited = temp
            if not temp:
                break
        return visited


def populated_graph():
    graph = Wgraph()
    graph.dict = {
        'a': ['b'],
        'b': ['c', 'd'],
        'c': ['b', 'a'],
        'd': ['c'],
        'e': []
        }
    return graph

def depth_populated_graph():
    graph = Wgraph()
    graph.dict = {
        'a': ['b', 'c', 'e'],
        'b': ['d', 'f'],
        'c': ['g'],
        'd': [],
        'e': [],
        'f': ['e'],
        'g': []
        }
    return graph


if __name__ == '__main__':
    temp = populated_graph()
    print "breadth"
    temp.breadth_first_traversal('a')
    print "depth"
    print temp.depth_first_traversal('a')

    temp2 = depth_populated_graph()
    print "depth_larger_cylce"
    print temp2.depth_first_traversal('a')
    print "breadth_larger_cycle"
    print temp2.breadth_first_traversal('a')








