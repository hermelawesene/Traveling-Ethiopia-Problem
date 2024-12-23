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

# Step 4: Visualize the graph
# Draw the graph with nodes and labels
pos = nx.spring_layout(G)  # You can experiment with different layouts (e.g., spring_layout, circular_layout, etc.)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=12, font_weight='bold')

# Add edge labels (distances) to the graph
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, font_color='red')

# Display the plot
plt.show()
