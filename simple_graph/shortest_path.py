from simple_graph.weighted_graph import Wgraph


def dijkstra(weighted_graph, start, end):

    list_of_tuples_node_totalweight = []
    list_of_tuples_node_totalweight.append((start, 0))
    # weight_dict[start] = 0          # total weight/distance
    prev = []         # previous node
    # unvisited = []

    for node in weighted_graph.nodes():
        if node is not start:
            list_of_tuples_node_totalweight.append(node, float("inf"))
        unvisited = list_of_tuples_node_totalweight

    while unvisited:
        sorted_list = sorted(unvisited, key=lambda x: x[1])
        temp = sorted_list[0]
        unvisited = sorted_list[1:]

        for neighbor in temp.neighbors():
            alt = temp[1] + weighted_graph[temp[0]][neighbor]
            if alt < list_of_tuples_node_totalweight[neighbor][1]:
                list_of_tuples_node_totalweight[neighbor][1] = alt
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