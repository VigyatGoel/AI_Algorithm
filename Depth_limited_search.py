graph = {

    'S': ['C', 'Z'],
    'C': ['D', 'B'],
    'Z': ['W'],
    'W': ['U'],
    'D': [],
    'B': [],
    'U': []
}


def depth_limited_search(graph, element, goal, depth):
    print(element, end=" ")

    if element == goal:
        return True

    if depth <= 0:
        return False

    for i in graph[element]:
        if depth_limited_search(graph, i, goal, depth - 1):
            return True
    return False




if __name__ == '__main__':
    if depth_limited_search(graph, "S", "W", 2):
        print("\nsuccess")
    else:
        print("\nFailure")
