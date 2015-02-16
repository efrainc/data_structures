#! /usr/bin/env python

# Simple Graph project for Efrain, Henry, Mark
# Graph is unweighted but directed


class Sgraph(object):
    """Instantiates simple graph"""

    def __init__(self):
        """Instantiates simple graph"""
        self.dict = {}

    def nodes(self):
        """return list of all nodes in a graph"""
        return self.dict.keys()

    def edges(self):
        """return a list of all edges in the graph"""
        output = []
        for k, v in self.dict:
            for val in v:
                output.append((k, val))
        return output

    def add_node(self, node):
        """adds a new node 'n' to the graph"""
        try:
            self.dict[node] = []
        except AttributeError:
            raise "Node Value must be unique non-integer"

    def has_node(self, n):
        """True if node 'n' is contained in the graph, False if not."""
        return n in self.dict

    def add_edge(self, n1, n2):
        """Adds a new edge to the graph connecting 'n1' and 'n2', if either n1 or n2 are not
        already present in the graph, they should be added."""
        if not self.has_node(n1):
            self.add_node(n1)
        if not self.has_node(n2):
            self.add_node(n2)
        self.dict[n1].append(n2)

    def del_node(self, n):
        """deletesthenode'n' from the graph, raises an error if no such node exists"""
        try:
            del self.dict[n]
        except (ValueError, KeyError):
                raise AttributeError('No Such Node Exists')

    def del_edge(self, n1, n2):
        """deletes the edge connecting 'n1' and 'n2' from the graph, raises an error if no
        such edge exists"""
        try:
            self.dict[n1].remove(n2)
        except (ValueError, KeyError):
            raise AttributeError('No Such Edge Exists')

    def neighbors(self, n):
        """returns the list of all nodes connected to 'n' by edges, raises an error if n is not in g"""
        return self.dict[n]

    def adjacent(self, n1, n2):
        """returns True if there is an edge connecting n1 and n2, False if not, raises an error if
        either of the supplied nodes are not in g"""
        return n2 in self.dict[n1] or n1 in self.dict[n2]


