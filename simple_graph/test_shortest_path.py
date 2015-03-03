import pytest
import weighted_graph as wgraph
from collections import OrderedDict
from shortest_path import dijkstra


def test_dijkstra_long_path(populated_graph1):
    """Test a graph with a shortest path with more nodes than longer path"""
    dist, path = dijkstra(populated_graph1, 'a', 'e')
    assert dist == 6
    assert path == ['a', 'c', 'd', 'e']


# def test_dijkstra_no_path(no_path_graph):
#     """Tests a graph where start and end do not connect"""
#     dist, path = dijkstra(no_path_graph, 'a', 'b')
#     assert False


# def test_dijkstra_short_cut(populated_graph2):
#     """Test a graph to see if it takes a low weight shortcut"""
#     dist, path = dijkstra(populated_graph2, 'a', 'e')
#     assert dist == 20
#     assert path == ['a', 'b', 'd', 'e']


@pytest.fixture(scope='function')
def populated_graph1():
    graph = wgraph.Wgraph()
    graph.dict = {
        'a': OrderedDict([('b', 10), ('c', 1), ('e', 20)]),
        'b': OrderedDict([('d', 7)]),
        'c': OrderedDict([('d', 2), ('e', 8)]),
        'd': OrderedDict([('e', 3)]),
        'e': OrderedDict()
        }
    return graph


@pytest.fixture(scope='function')
def populated_graph2():
    graph = wgraph.Wgraph()
    graph.dict = {
        'a': OrderedDict([('b', 4)]),
        'b': OrderedDict([('c', 5), ('d', 1)]),
        'c': OrderedDict([('d', 6)]),
        'd': OrderedDict([('e', 7)]),
        'e': OrderedDict([('f', 8)])
        }
    return graph


@pytest.fixture(scope='function')
def no_path_graph():
    graph = wgraph.Wgraph()
    graph.dict = {
        'a': OrderedDict(),
        'b': OrderedDict()
        }
    return graph
