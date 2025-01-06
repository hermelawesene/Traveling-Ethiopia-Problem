import queue

def bfs_path(graph, start, goal):
    visited = set()
    q = queue.Queue()
    q.put((start, [start]))  # (current_node, path)

    while not q.empty():
        current, path = q.get()
        if current == goal:
            return path, len(path) - 1  # Number of steps (unweighted BFS)
        if current not in visited:
            visited.add(current)
            for neighbor in graph.neighbors(current):
                if neighbor not in visited:
                    q.put((neighbor, path + [neighbor]))
    return None, 0

def bfs_traverse(graph, start, visited):
    q = queue.Queue()
    q.put((start, 0))  # (current_city, cumulative_cost)
    path = []
    total_cost = 0

    while not q.empty():
        current, cost = q.get()
        if current not in visited:
            visited.add(current)
            path.append(current)
            total_cost += cost
            for neighbor, data in graph[current].items():
                if neighbor not in visited:
                    q.put((neighbor, data['weight']))
    return path, total_cost