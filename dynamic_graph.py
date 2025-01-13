import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs_traverse(roads, start_city):
    """
    Perform BFS traversal to visit all cities starting from the given city.

    Parameters:
    - roads: Dictionary with city connections as {city: [(connected_city, distance)]}.
    - start_city: The city to start the traversal.

    Returns:
    - path: List of cities representing the traversal path.
    - cost: Total cost (distance) of the traversal.
    """
    visited = set()
    queue = deque([start_city])
    path = []
    cost = 0

    while queue:
        current_city = queue.popleft()
        if current_city not in visited:
            visited.add(current_city)
            path.append(current_city)
            for neighbor, distance in roads.get(current_city, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    cost += distance  # Add cost only when encountering a new connection

    return path, cost


def visualize_graph(roads, blocked_edges=None, traversal_path=None, title="Graph Visualization"):
    """
    Dynamically visualizes the graph based on input data.

    Parameters:
    - roads: Dictionary with city connections as {city: [(connected_city, distance)]}.
    - blocked_edges: List of edges (tuples) to highlight as blocked.
    - traversal_path: List of cities representing a path to highlight.
    - title: Title of the plot.
    """
    # Create the graph from the roads dictionary
    graph = nx.Graph()
    for city, connections in roads.items():
        for connected_city, distance in connections:
            graph.add_edge(city, connected_city, weight=distance)

    # Draw the graph
    pos = nx.spring_layout(graph)  # Layout for positioning nodes
    nx.draw(graph, pos, with_labels=True, node_color="lightblue", node_size=1500, font_size=10)
    nx.draw_networkx_edge_labels(
        graph,
        pos,
        edge_labels={(u, v): f"{d['weight']} km" for u, v, d in graph.edges(data=True)},
        font_color="green",
    )

    # Highlight blocked edges
    if blocked_edges:
        nx.draw_networkx_edges(
            graph,
            pos,
            edgelist=blocked_edges,
            edge_color="red",
            width=2,
            style="dashed",
            label="Blocked Roads",
        )

    # Highlight traversal path
    if traversal_path:
        path_edges = list(zip(traversal_path, traversal_path[1:]))
        nx.draw_networkx_edges(
            graph,
            pos,
            edgelist=path_edges,
            edge_color="blue",
            width=3,
            style="solid",
            label="Traversal Path",
            arrows=True,
        )

    # Add legend and title
    plt.legend()
    plt.title(title)
    plt.show()


# Main Program
if __name__ == "__main__":
    # Define the road network
    roads = {
        'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
        'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
        'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
        'Hawassa': [('Addis Ababa', 275)],
        'Mekelle': [('Gondar', 300)]
    }

    # Define starting city and strategy
    start_city = "Addis Ababa"

    # Perform BFS traversal
    traversal_path, total_cost = bfs_traverse(roads, start_city)
    print(f"BFS Path: {traversal_path} with cost {total_cost}")

    # Define blocked road dynamically (from logic or example)
    blocked_road = [('Addis Ababa', 'Hawassa')]

    # Visualize graph with traversal path and blocked roads
    visualize_graph(
        roads=roads,
        blocked_edges=blocked_road,
        traversal_path=traversal_path,
        title="Dynamic Ethiopia Road Network Visualization"
    )
