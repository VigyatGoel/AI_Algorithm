import heapq

graph = {
    'V': [('I', 2), ('G', 5)],
    'I': [('G', 1), ('Y', 13)],
    'G': [('A', 3)],
    'A': [('Y', 4)],
    'Y': [],
}

heuristic = {
    'V': 8,
    'I': 7,
    'G': 3,
    'A': 2,
    'Y': 0,
}


def Astar(graph, start, goal, heuristic):
    open_list = [(0, start)]
    closed_list = set()

    path_costs = {node: float('inf') for node in graph}
    path_costs[start] = 0

    parent = {}

    while open_list:

        _, current_node = heapq.heappop(open_list)

        if current_node not in closed_list:

            closed_list.add(current_node)

            for child_node, cost in graph[current_node]:

                new_path_cost = path_costs[current_node] + cost

                f_cost = new_path_cost + heuristic[child_node]

                if child_node not in path_costs or f_cost < path_costs[child_node] + heuristic[child_node]:
                    path_costs[child_node] = new_path_cost

                    heapq.heappush(open_list, (f_cost, child_node))

                    parent[child_node] = current_node

        if current_node == goal:

            path = [current_node]
            while current_node != start:
                current_node = parent[current_node]
                path.append(current_node)
            path.reverse()
            return path

    return None


path = Astar(graph, 'V', 'Y', heuristic)
print("Path:", path)
