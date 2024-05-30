graph = {
    '6': ['3', '4'],
    '3': ['7', '2'],
    '4': ['8'],
    '7': [],
    '2': [],
    '8': []
}


def bfs(graph, start):
    open = []
    closed = []

    open.append(start)
    closed.append(start)

    while open:
        element = open.pop(0)
        print(element, end=" ")

        for neighbor in graph[element]:
            if neighbor not in closed:
                open.append(neighbor)
                closed.append(neighbor)


if __name__ == '__main__':
    bfs(graph, "6")
