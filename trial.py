import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Create an empty graph
G = nx.Graph()

# Step 2: Add cities as nodes
cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
for city in cities:
    G.add_node(city)

# Step 3: Add roads as edges with distances
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}

# Add edges between cities (with weights representing distances)
for city, connections in roads.items():
    for connected_city, distance in connections:
        G.add_edge(city, connected_city, weight=distance)

# Add edge labels (distances)
edge_list = nx.get_edge_attributes(G, 'weight')

# Step 4: Visualize the graph
nx.draw(G, with_labels=True, node_size=3000, node_color='lightblue', font_size=12, font_weight='bold')
plt.show()
nx.draw_spring(G, with_lables = True, )
G.add_edge(edge_list)
plt.show()