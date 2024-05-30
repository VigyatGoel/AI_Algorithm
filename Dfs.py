graph = {
    '6': ['3', '4'],
    '3': ['7', '2'],
    '4': ['8'],
    '7': [],
    '2': [],
    '8': []
}


def dfs(graph, start):
    open = []
    closed = []
    open.append(start)
    closed.append(start)

    while open:
        element = open.pop()
        print(element, end=" ")

        for i in graph[element]:
            dfs(graph, i)


if __name__ == '__main__':
    dfs(graph, '6')
