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