from weighted_graph import Wgraph
import copy


def dijkstra(weighted_graph, start, end):

    list_of_tuples_node_totalweight = []
    list_of_tuples_node_totalweight.append((start, 0))
    # weight_dict[start] = 0          # total weight/distance
    prev = []         # previous node
    # unvisited = []

    for node in weighted_graph.nodes():
        if node is not start:
            list_of_tuples_node_totalweight.append((node, float("inf")))
        unvisited = copy.deepcopy(list_of_tuples_node_totalweight)
        print "unvisited " + str(unvisited)

    while unvisited:
        sorted_list = sorted(unvisited, key=lambda x: x[1])
        print "sorted: " + str(sorted_list)
        temp = sorted_list[0]
        unvisited = sorted_list[1:]

        for neighbor in weighted_graph.neighbors(temp[0]):
            alt = temp[1] + weighted_graph.dict[temp[0]][neighbor]
            print "neighbor " + neighbor
            holder = [weight for node, weight in enumerate(list_of_tuples_node_totalweight) if node  == neighbor]
            if alt < holder:
                list_of_tuples_node_totalweight.pop(
                    list_of_tuples_node_totalweight.index((neighbor, holder)))
                list_of_tuples_node_totalweight.append((neighbor, alt))
                prev.append(neighbor)
                if temp == end:
                    break
    return list_of_tuples_node_totalweight, prev



    # already_visited = [start]
    # for node in weighted_graph:
    #     if node is not start:
    #         weight = 100
    #         # previous = undefined
    #     pq = Pq.insert(node, weight)

    # while Pq:
    #     temp = pq.pop()
    #     for neighbor in weighted_graph.neighbors(temp):
    #         alt =