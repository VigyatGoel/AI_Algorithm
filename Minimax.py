tree = {
    'E': ['F', 'G'],
    'F': ['H', 'I'],
    'G': ['J', 'K'],
    'H': ['L', 'M'],
    'I': ['N', 'O'],
    'J': ['P', 'Q'],
    'K': ['R', 'S']
}

terminal_nodes = {
    'L': 1,
    'M': -2,
    'N': 3,
    'O': -4,
    'P': 5,
    'Q': -6,
    'R': 7,
    'S': -8
}


def minimax(node, depth, is_max_player):
    if node in terminal_nodes:
        return terminal_nodes[node], [node]

    if is_max_player:
        best_value = float('-inf')
        best_path = []
        for child in tree[node]:
            current_value, path = minimax(child, depth + 1, False)

            if current_value > best_value:
                best_value = current_value
                best_path = path

        best_path.insert(0, node)
        return best_value, best_path
    else:
        best_value = float('inf')
        best_path = []
        for child in tree[node]:
            current_value, path = minimax(child, depth + 1, True)
            if current_value < best_value:
                best_value = current_value
                best_path = path
        best_path.insert(0, node)
        return best_value, best_path


optimal_value, optimal_path = minimax('E', 0, True)

print("The optimal value is: ", optimal_value, "and path is: ", optimal_path)
