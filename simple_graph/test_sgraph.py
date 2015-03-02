import pytest
import sgraph


def test___init__():
    """Test instantiates simple graph with dictionary."""
    assert sgraph.Sgraph().dict == {}


def test_nodes(empty_graph, populated_graph):
    """Test return list of all nodes in a graph"""
    assert empty_graph.nodes() == []
    l = ['a', 'b', 'c', 'd', 'e']
    sortedlist = populated_graph.nodes()
    sortedlist.sort()
    assert sortedlist == l


def test_edges(populated_graph):
    """Test return a list of all edges in the graph"""
    edges = [('a', 'b'), ('b', 'c'), ('c', 'b'),
             ('c', 'a'), ('b', 'd'), ('d', 'c')]
    for edge in edges:
        assert edge in populated_graph.edges()


def test_add_node_empty(empty_graph):
    """Test adds a new node 'n' to the empty graph"""
    empty_graph.add_node('a')
    assert empty_graph.has_node('a')


def test_add_node_populated(populated_graph):
    """Test adds a new node 'n' to the populated graph"""
    populated_graph.add_node('g')
    assert populated_graph.has_node('g')


def test_has_node(empty_graph, populated_graph):
    """Test True if node 'n' is contained in the graph, False if not."""
    assert empty_graph.has_node('a') is False
    l = ['a', 'b', 'c', 'd', 'e']
    for node in l:
        assert populated_graph.has_node(node) is True
    assert populated_graph.has_node('t') is False


def test_add_edge_empty(empty_graph):
    """Test Adds a new edge to the graph connecting 'n1' and 'n2', if either n1 or n2 are not
    already present in the graph, they should be added."""
    empty_graph.add_edge('a', 'b')
    assert empty_graph.has_node('a')
    assert empty_graph.has_node('b')
    assert empty_graph.dict['a'] == ['b']


def test_del_node_empty(empty_graph):
    """Test deletesthenode'n' from the graph, raises an error if no such node exists"""
    with pytest.raises(AttributeError):
        empty_graph.del_node('a')


def test_del_node_populated(populated_graph):
    """Test deletesthenode'n' from the graph, raises an error if no such node exists"""
    populated_graph.del_node('a')
    assert not populated_graph.has_node('a')
    assert 'a' not in populated_graph.dict['c']


def test_del_edge_empty(empty_graph):
    """Test deletes the edge connecting non-existing 'n1' and 'n2' from the graph,
    raises an error if no such edge exists"""
    with pytest.raises(AttributeError):
        empty_graph.del_edge('a', 'b')


def test_del_edge_empty(populated_graph):
    """Test deletes the edge connecting 'n1' and 'n2' from the graph"""
    populated_graph.del_edge('a', 'b')
    assert 'b' not in populated_graph.dict['a']


def test_neighbors(populated_graph):
    """Test returns the list of all nodes connected to 'n' by edges, raises an error if n is not in g"""
    l = ['a', 'b']
    for node in l:
        assert node in populated_graph.neighbors('c')



def test_adjacent_empty(empty_graph):
    """Test returns True if there is an edge connecting n1 and n2, False if not, raises an error if
    either of the supplied nodes are not in g"""
    with pytest.raises(KeyError):
        empty_graph.adjacent('a', 'b')


def test_adjacent_pop(populated_graph):
    """Test returns True if there is an edge connecting n1 and n2, False if not, raises an error if
    either of the supplied nodes are not in g"""
    assert populated_graph.adjacent('a', 'b')
    assert not populated_graph.adjacent('a', 'd')

def test_depth_first_traversal(depth_populated_graph):
    """Test the depth first tranversal approach for a graph of arbitrary length"""
    assert depth_populated_graph.depth_first_traversal('a') == ['a', 'b', 'd', 'f', 'e', 'c', 'g']

def test_breadth_first_traversal(breadth_populated_graph):
    """Test the breadth first tranversal approach for a graph of arbitrary length"""
    assert breadth_populated_graph.breadth_first_traversal('a') == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def test_breadth_with_cycle(populated_graph):
    """Test the depth first tranversal approach for a graph of arbitrary length and a cycle"""
    assert populated_graph.breadth_first_traversal('a') == ['a', 'b', 'c', 'd']

@pytest.fixture(scope='function')
def empty_graph():
    graph = sgraph.Sgraph()
    return graph


@pytest.fixture(scope='function')
def populated_graph():
    graph = sgraph.Sgraph()
    graph.dict = {
        'a': ['b'],
        'b': ['c', 'd'],
        'c': ['b', 'a'],
        'd': ['c'],
        'e': []
        }
    return graph

@pytest.fixture(scope='function')
def depth_populated_graph():
    graph = sgraph.Sgraph()
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

@pytest.fixture(scope='function')
def breadth_populated_graph():
    graph = sgraph.Sgraph()
    graph.dict = {
        'a': ['b', 'c'],
        'b': ['d', 'e'],
        'c': ['f', 'g'],
        'd': [],
        'e': ['h'],
        'f': [],
        'g': [],
        'h': [],
        }
    return graph