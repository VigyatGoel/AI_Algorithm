graph = {

    'S': ['C', 'Z'],
    'C': ['D', 'B'],
    'Z': ['W'],
    'W': ['U'],
    'D': [],
    'B': [],
    'U': []
}


def depth_limited_search(graph, element, goal, depth, max_depth):
    print(element, end=" ")

    if element == goal:
        return True

    if depth == max_depth:
        return False

    for i in graph[element]:
        if depth_limited_search(graph, i, goal, depth + 1, max_depth):
            return True
    return False


def iddfs(graph, start, goal, max_depth):
    for i in range(max_depth):
        print(f"\nDepth {i}")
        if depth_limited_search(graph, start, goal, 0, i):
            return True
    return False

print(iddfs(graph, "S", "W", 3))


