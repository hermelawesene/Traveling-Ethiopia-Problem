import networkx as nx
from heapq import heappush, heappop
import matplotlib.pyplot as plt

def k_shortest_paths(graph, start, goal, k=3):
    """
    Finds the k-shortest paths between two cities.
    
    Parameters:
    - graph: The NetworkX graph representing the road network.
    - start: Starting city.
    - goal: Destination city.
    - k: Number of shortest paths to find.

    Returns:
    - paths: A list of k shortest paths with their respective costs.
    """
    paths = []
    queue = [(0, start, [start])]  # (cumulative_cost, current_city, path)

    while queue and len(paths) < k:
        cost, current, path = heappop(queue)
        if current == goal:
            paths.append((path, cost))
            continue
        for neighbor in graph.neighbors(current):
            if neighbor not in path:  # Avoid cycles
                edge_cost = graph[current][neighbor]['weight']
                heappush(queue, (cost + edge_cost, neighbor, path + [neighbor]))
    return paths

def visualize_paths(graph, paths, title="k-Shortest Paths"):
    """
    Visualize the k-shortest paths on the graph.

    Parameters:
    - graph: The NetworkX graph representing the road network.
    - paths: List of paths with their costs to visualize.
    - title: Title for the visualization.
    """
    pos = nx.spring_layout(graph)  # Layout for graph nodes
    nx.draw(graph, pos, with_labels=True, node_color="lightblue", node_size=1500, font_size=10)
    nx.draw_networkx_edge_labels(
        graph,
        pos,
        edge_labels={(u, v): f"{d['weight']} km" for u, v, d in graph.edges(data=True)},
        font_color="green",
    )
    
    # Highlight each path with different colors
    colors = ['blue', 'orange', 'purple', 'red', 'green']
    for i, (path, cost) in enumerate(paths):
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(
            graph,
            pos,
            edgelist=path_edges,
            edge_color=colors[i % len(colors)],
            width=3,
            label=f"Path {i+1}: {cost} km"
        )
    
    plt.legend()
    plt.title(title)
    plt.show()

# Example usage
if __name__ == "__main__":
    # Create a graph
    roads = {
        'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
        'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
        'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
        'Hawassa': [('Addis Ababa', 275)],
        'Mekelle': [('Gondar', 300)]
    }

    graph = nx.Graph()
    for city, connections in roads.items():
        for connected_city, distance in connections:
            graph.add_edge(city, connected_city, weight=distance)

    # Find k-shortest paths
    k = 2
    start = 'Addis Ababa'
    goal = 'Mekelle'
    paths = k_shortest_paths(graph, start, goal, k)

    # Print paths and costs
    for i, (path, cost) in enumerate(paths, start=1):
        print(f"Path {i}: {path} with cost {cost}")

    # Visualize the paths
    visualize_paths(graph, paths, title=f"{k}-Shortest Paths from {start} to {goal}")
