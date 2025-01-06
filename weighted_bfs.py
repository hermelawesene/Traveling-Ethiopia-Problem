import queue

def weighted_bfs(graph, start, goal):
    visited = set()
    pq = queue.PriorityQueue()
    pq.put((0, start, [start]))  # (cumulative_cost, current_node, path)

    while not pq.empty():
        cost, current, path = pq.get()
        if current == goal:
            return path, cost  # Total distance (weighted BFS)
        if current not in visited:
            visited.add(current)
            for neighbor in graph.neighbors(current):
                if neighbor not in visited:
                    edge_cost = graph[current][neighbor]['weight']
                    pq.put((cost + edge_cost, neighbor, path + [neighbor]))
    return None, 0
