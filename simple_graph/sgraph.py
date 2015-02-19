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
        return [(k, val) for k, v in self.dict.iteritems() for val in v]

    def add_node(self, node):
        """adds a new node 'n' to the graph. Nodes must be hashable values."""
        try:
            self.dict.setdefault(node, [])
        except (AttributeError, TypeError):
            raise "Node Value must be unique non-integer"

    def has_node(self, n):
        """True if node 'n' is contained in the graph, False if not."""
        return n in self.dict

    def add_edge(self, n1, n2):
        """Adds a new edge to the graph connecting 'n1' to 'n2', if either n1
        or n2 are not already present in the graph, they should be added."""
        self.add_node(n1)
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
        """Returns the list of all nodes with edges leading to them from n,
        raise error if n is not in g."""

        try:
            return self.dict[n]
        except KeyError:
            raise KeyError('Node not in graph.')

    def adjacent(self, n1, n2):
        """returns True if there is an edge connecting n1 and n2, False if not,
        raises an error if either of the supplied nodes are not in g."""
        try:
            return n2 in self.dict[n1]
        except KeyError:
            raise KeyError('Node(s) not in graph.')

    def depth_first_traversal(self, start, visited=[]):
        """Perform a full depth-first traversal of the graph beginning at start.
        Return the path when complete."""
        if start not in visited:
            visited.append(start)
            for i in self.neighbors(start):
                self.depth_first_traversal(i, visited)
            return visited


    def breath_first_traversal(self, start, visited=[]):
        """Perform a full breadth-first traversal of the graph beginning at start.
        Return the path when complete."""
        if start not in visited:
            visited.append(start)
        start_visited = visited
        while True:
            visited = self.get_all_neighbors(start_visited, visited)
            start_visited = visited-start_visited
            if visited-start_visited == None:
                break

    def get_all_neighbors(self, start_visited, visited):
        """for all neighors in node, return list of"""
        for node_ in start_visited:
            for i in self.neighbors(node_):
                if i not in visited:
                    visited.append(i)
        return visited






