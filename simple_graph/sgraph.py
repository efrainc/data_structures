#! /usr/bin/env python

# Simple Graph project for Efrain, Henry, Mark
# Graph is unweighted but directed


class Sgraph(object):
    """A class defining a unweighted direct simple graph."""

    def __init__(self):
        """Instantiates simple graph"""
        self.dict = {}

    def nodes(self):
        """return list of all nodes in a graph"""
        return self.dict.keys()

    def edges(self):
        """return a list of all edges in the graph"""
        output = []
        for k, v in self.dict.iteritems():
            for val in v:
                output.append((k, val),)
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
        """Adds a new edge to the graph connecting 'n1' and 'n2', if either n1
        or n2 are not already present in the graph, they should be added."""
        if not self.has_node(n1):
            self.add_node(n1)
        if not self.has_node(n2):
            self.add_node(n2)
        self.dict[n1].append(n2)

    def del_node(self, n):
        """Delete 'n' from the graph, raise error if node doesn't exist."""
        try:
            del self.dict[n]
            # remove edges pointing to n
            for value in self.dict.itervalues():
                if n in value:
                    value.remove(n)
        except (ValueError, KeyError):
                raise AttributeError('No Such Node Exists')

    def del_edge(self, n1, n2):
        """Delete edge connecting 'n1' and 'n2' from the graph, raise
        error if edge doesn't exist."""
        try:
            self.dict[n1].remove(n2)
        except (ValueError, KeyError):
            raise AttributeError('No Such Edge Exists')

    def neighbors(self, n):
        """Returns the list of all nodes connected to 'n' by edges,
        raise error if n is not in g."""
        out = self.dict[n]
        for keys, values in self.dict.items():
            if n in values:
                out.append(keys)
        return set(out)

    def adjacent(self, n1, n2):
        """returns True if there is an edge connecting n1 and n2, False if not,
        raises an error if either of the supplied nodes are not in g."""
        try:
            return n2 in self.dict[n1] or n1 in self.dict[n2]
        except KeyError:
            raise KeyError('Node(s) not in graph.')
