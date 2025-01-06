import networkx as nx

def build_graph(roads):
    G = nx.Graph()
    for city, connections in roads.items():
        for connected_city, distance in connections:
            G.add_edge(city, connected_city, weight=distance)
    return G
