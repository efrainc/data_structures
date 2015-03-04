from Queue import PriorityQueue
import weighted_graph as wgraph
from collections import OrderedDict
import copy
import time


def timed_func(func):
    """Decorator for timing our traversal methods."""
    def timed(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print "time expired: %s" % elapsed
        return result
    return timed

@timed_func
def dijkstra(weighted_graph, start, end):
    """Dijkstra algorithm with list of tuples and full iteration"""
    list_of_tuples_node_totalweight = []
    list_of_tuples_node_totalweight.append((start, 0))
    # weight_dict[start] = 0          # total weight/distance
    prev = []         # previous node
    # unvisited = []

    for node in weighted_graph.nodes():
        if node is not start:
            list_of_tuples_node_totalweight.append((node, float("inf")))
        unvisited = copy.deepcopy(list_of_tuples_node_totalweight)

    while unvisited:
        sorted_list = sorted(unvisited, key=lambda x: x[1])
        temp = sorted_list[0]
        for i, j in list_of_tuples_node_totalweight:
            if i == temp[0]:
                new_temp = j

        for neighbor in weighted_graph.neighbors(temp[0]):
            alt = new_temp + weighted_graph.dict[temp[0]][neighbor]
            for i, j in list_of_tuples_node_totalweight:
                if i == neighbor:
                    list_v = j

            if alt < list_v:
                list_of_tuples_node_totalweight.remove((neighbor, list_v))
                list_of_tuples_node_totalweight.append((neighbor, alt))
                prev.append(neighbor)
                # if temp == end:
                #     break
        unvisited = sorted_list[1:]
    return list_of_tuples_node_totalweight[-1][1]


@timed_func
def dijkstraPQ(weighted_graph, start, end):
    """Dijkstra algorithm with PQ."""
    dict_node_totalweight = {}
    dict_node_totalweight[start] = 0
    pq = PriorityQueue()
    pq.put((0, start))
    for node in weighted_graph.nodes():
        if node is not start:
            dict_node_totalweight[node] = float("inf")
        pq.put((float("inf"), node))

    while pq:
        temp = pq.get()
        # test if at node with no neighbors (lowest value is inf)
        if temp[0] == float("inf"):
            break
        # compute weights for all neighbors
        for neighbor in weighted_graph.neighbors(temp[1]):
            alt = temp[0] + weighted_graph.dict[temp[1]][neighbor]
            if alt < dict_node_totalweight.get(neighbor):
                # print 'new weight = {}'.format(alt)
                dict_node_totalweight[neighbor] = alt
                pq.put((alt, neighbor))
        # Check if we've reached our destination
        if temp[1] == end:
            break
    # print 'weight: {}'.format(dict_node_totalweight[end])
    return dict_node_totalweight[end]

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


if __name__ == '__main__':
    temp = populated_graph1()
    print "Dijkstra"
    print dijkstra(temp, 'a', 'e')
    print "DijkstraPQ"
    print dijkstraPQ(temp, 'a', 'e')



