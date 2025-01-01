import queue
import networkx as nx
import matplotlib.pyplot as plt
import time


def uninformed_path_finder(cities, roads, start_city, goal_city, strategy):
    """
    Parameters:
    - cities: List of city names.
    - roads: Dictionary with city connections as {city: [(connected_city, distance)]}.
    - start_city: The city to start the journey.
    - goal_city: The destination city (for specific tasks).
    - strategy: The uninformed search strategy to use ('bfs', 'dfs', 'weighted_bfs').
    
    Returns:
    - path: List of cities representing the path from start_city to goal_city.
    - cost: Total cost (number of steps or distance) of the path.
    """
    graph = build_graph(roads)
    
    if strategy == 'bfs':
        return bfs_path(graph, start_city, goal_city)
    elif strategy == 'dfs':
        return dfs_path(graph, start_city, goal_city)
    elif strategy == 'weighted_bfs':
        return weighted_bfs(graph, start_city, goal_city)
    else:
        raise ValueError("Invalid strategy! Choose from 'bfs', 'dfs', or 'weighted_bfs'.")


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


def build_graph(roads):
    G = nx.Graph()
    for city, connections in roads.items():
        for connected_city, distance in connections:
            G.add_edge(city, connected_city, weight=distance)
    return G


# Visualization
def visualize_search(order, title, G, pos):
    plt.figure()
    plt.title(title)
    for i, node in enumerate(order, start=1):
        plt.clf()
        plt.title(title)
        nx.draw(G, pos, with_labels=True, node_color=['r' if n == node else 'g' for n in G.nodes])
        plt.draw()
        plt.pause(1.5)
    plt.show()
    time.sleep(0.5)


# Data
cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}

# Main
start_city = 'Addis Ababa'
goal_city = 'Mekelle'
strategy = 'weighted_bfs'  # Choose 'bfs', 'dfs', or 'weighted_bfs'

G = build_graph(roads)
pos = nx.circular_layout(G)

# Run the selected strategy
path, cost = uninformed_path_finder(cities, roads, start_city, goal_city, strategy)
print(f"Strategy: {strategy.capitalize()}")
print(f"Path: {path}")
print(f"Cost: {cost}")

# Highlight the path
if path:
    visualize_search(path, f"Path using {strategy.capitalize()}", G, pos)
