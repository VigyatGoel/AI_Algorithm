from collections import deque


def heuristic(state, goal):
    return sum(abs(state[i] - goal[i]) for i in range(len(state)))


def pour(state, jug1, jug2):
    pour_amt = min(state[jug1], (jug_caps[jug2] - state[jug2]))
    new_state = list(state)
    new_state[jug1] -= pour_amt
    new_state[jug2] += pour_amt
    return tuple(new_state)


def get_states(state):
    successors = []
    for jug1, jug2 in [(0, 1), (1, 0)]:
        new_state = pour(state, jug1, jug2)
        if new_state != state:
            successors.append(new_state)
    for jug in [0, 1]:
        new_state = list(state)
        new_state[jug] = jug_caps[jug]
        successors.append(tuple(new_state))
    for jug in [0, 1]:
        new_state = list(state)
        new_state[jug] = 0
        successors.append(tuple(new_state))
    return successors


def water_jug_problem(start, goal):
    open_list = [(heuristic(start, goal), start)]
    closed_list = set()
    parent = {start: None}
    g_cost = {start: 0}

    while open_list:
        _, curr_state = open_list.pop(0)
        if curr_state == goal:
            path = deque()
            state = curr_state
            while state is not None:
                path.appendleft(state)
                state = parent[state]
            return list(path)
        closed_list.add(curr_state)
        for succ_state in get_states(curr_state):
            if succ_state not in closed_list:
                new_g_cost = g_cost[curr_state] + 1
                if succ_state not in g_cost or new_g_cost < g_cost[succ_state]:
                    g_cost[succ_state] = new_g_cost
                    f_cost = new_g_cost + heuristic(succ_state, goal)
                    open_list.append((f_cost, succ_state))
                    parent[succ_state] = curr_state
                    open_list.sort()
    return None


jug_caps = (4, 3)
start_state = (0, 0)
goal_state = (2, 3)
solution = water_jug_problem(start_state, goal_state)

if __name__ == '__main__':
    if solution:
        print("Solution:")
        for state in solution:
            print(state)
    else:
        print("No solution exists.")