import pytest
import sgraph


def test___init__():
    """ Test Instantiates simple graph"""
    assert False


def test_nodes(empty_graph, populated_graph):
    """ Test return list of all nodes in a graph"""
    print "populated_graph:  " + str(populated_graph.nodes())
    assert empty_graph.nodes() == []
    l = ['a', 'b', 'c', 'd', 'e']
    sortedlist = populated_graph.nodes()
    sortedlist.sort()
    assert sortedlist == l


def test_edges(empty_graph, populated_graph):
    """ Test return a list of all edges in the graph"""
    edges = [('a', 'b'), ('b', 'c'), ('c', 'b'),
             ('c', 'a'), ('b', 'd'), ('d', 'c')]
    for edge in edges:
        assert edge in populated_graph.edges()


def test_add_node(empty_graph, populated_graph):
    """ Test adds a new node 'n' to the graph"""
    assert False


def test_has_node(empty_graph, populated_graph):
    """ Test True if node 'n' is contained in the graph, False if not."""
    assert empty_graph.has_node('a') is False
    l = ['a', 'b', 'c', 'd', 'e']
    for node in l:
        assert populated_graph.has_node(node) is True
    assert populated_graph.has_node('t') is False


def test_add_edge(empty_graph, populated_graph):
    """ Test Adds a new edge to the graph connecting 'n1' and 'n2', if either n1 or n2 are not
    already present in the graph, they should be added."""
    assert False


def test_del_node(empty_graph, populated_graph):
    """ Test deletesthenode'n' from the graph, raises an error if no such node exists"""
    
    assert False


def test_del_edge(empty_graph, populated_graph):
    """ Test deletes the edge connecting 'n1' and 'n2' from the graph, raises an error if no
    such edge exists"""
    assert False

def test_neighbors(empty_graph, populated_graph):
    """ Test returns the list of all nodes connected to 'n' by edges, raises an error if n is not in g"""
    assert False


def test_adjacent(empty_graph, populated_graph):
    """ Test returns True if there is an edge connecting n1 and n2, False if not, raises an error if
    either of the supplied nodes are not in g"""
    assert False


@pytest.fixture(scope='function')
def empty_graph():
    graph = sgraph.Sgraph()
    return graph


@pytest.fixture(scope='function')
def populated_graph():
    graph = sgraph.Sgraph()
    l = ['a', 'b', 'c', 'd', 'e']
    for node in l:
        graph.add_node(node)
    edges = [('a', 'b'), ('b', 'c'), ('c', 'b'),
             ('c', 'a'), ('b', 'd'), ('d', 'c')]
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    return graph
