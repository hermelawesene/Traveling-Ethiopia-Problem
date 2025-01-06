def dfs_path(graph, start, goal):
    visited = set()
    stack = [(start, [start])]  # (current_node, path)

    while stack:
        current, path = stack.pop()
        if current == goal:
            return path, len(path) - 1  # Number of steps (unweighted DFS)
        if current not in visited:
            visited.add(current)
            for neighbor in graph.neighbors(current):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None, 0


def dfs_traverse(graph, start, visited):
    stack = [(start, 0)]  # (current_city, cumulative_cost)
    path = []
    total_cost = 0

    while stack:
        current, cost = stack.pop()
        if current not in visited:
            visited.add(current)
            path.append(current)
            total_cost += cost
            for neighbor, data in graph[current].items():
                if neighbor not in visited:
                    stack.append((neighbor, data['weight']))
    return path, total_cost
