import math

INFINITY = math.inf
NEG_INFINITY = -math.inf

game_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': []
}
terminal_nodes = {
    'H': 2,
    'I': 4,
    'J': 5,
    'K': 8,
    'L': 0,
    'M': 1,
    'N': -1,
    'O': 1
}


def alpha_beta_pruning(node, depth, alpha, beta, max_player):
    if depth == 0 or node not in game_tree or not game_tree[node]:
        return terminal_nodes[node], [node]

    if max_player:
        best_path = []
        for child in game_tree[node]:
            value, path = alpha_beta_pruning(child, depth - 1, alpha, beta, False)
            if value > alpha:
                alpha = value
                best_path = [node] + path
            if beta <= alpha:
                break
        return alpha, best_path
    else:
        best_path = []
        for child in game_tree[node]:
            value, path = alpha_beta_pruning(child, depth - 1, alpha, beta, True)
            if value < beta:
                beta = value
                best_path = [node] + path
            if beta <= alpha:
                break
        return beta, best_path


def main():
    root = 'A'
    depth = 3
    alpha = NEG_INFINITY
    beta = INFINITY
    max_player = True

    optimal_value, optimal_path = alpha_beta_pruning(root, depth, alpha, beta, max_player)
    print(f"The optimal value is: {optimal_value}")
    print(f"The path to the optimal value is: {' -> '.join(optimal_path)}")


if __name__ == '__main__':
    main()
