import networkx as nx
import matplotlib.pyplot as plt
import time
from bfs import bfs_path
from dfs import dfs_path
from weighted_bfs import weighted_bfs

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
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275), ('Dire Dawa', 400)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180), ('Mekelle', 600)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275), ('Dire Dawa', 450)],
    'Dire Dawa': [('Addis Ababa', 400), ('Hawassa', 450), ('Mekelle', 700)],
    'Mekelle': [('Bahir Dar', 600), ('Gondar', 300), ('Dire Dawa', 700)]
}


# Main

start_city = 'Gondar'
goal_city = 'Hawassa'
strategy = 'weighted_bfs'  # Choose 'bfs', 'dfs', or 'weighted_bfs'

G = build_graph(roads)
pos = nx.circular_layout(G)

# Run the selected strategy
if strategy == 'bfs':
    path, cost = bfs_path(G, start_city, goal_city)
elif strategy == 'dfs':
    path, cost = dfs_path(G, start_city, goal_city)
elif strategy == 'weighted_bfs':
    path, cost = weighted_bfs(G, start_city, goal_city)
else:
    raise ValueError("Invalid strategy! Choose from 'bfs', 'dfs', or 'weighted_bfs'.")

print(f"Strategy: {strategy.capitalize()}")
print(f"Path: {path}")
print(f"Cost: {cost}")

# Highlight the path
if path:
    visualize_search(path, f"Path using {strategy.capitalize()}", G, pos)
