import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue, Queue, LifoQueue

# Data
cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}

# Build Graph  
def build_graph(roads):
    G = nx.Graph()
    for city, connections in roads.items():
        for connected_city, distance in connections:
            G.add_edge(city, connected_city, weight=distance)
    return G


# Main
G = build_graph(roads)
start_city = 'Addis Ababa'
goal_city = 'Mekelle'
nx.draw_spring(G, with_lables = True)
#G.add_edge(edge_list)
plt.show()