from bfs import bfs_traverse
from dfs import dfs_traverse
from graph import build_graph

def traverse_all_cities(cities, roads, start_city, strategy):
    
    graph = build_graph(roads)
    visited = set()
    path = []
    cost = 0

    if strategy == 'bfs':
        traversal_func = bfs_traverse
    elif strategy == 'dfs':
        traversal_func = dfs_traverse
    else:
        raise ValueError("Invalid strategy! Choose 'bfs' or 'dfs'.")

    traversal_path, traversal_cost = traversal_func(graph, start_city, visited)
    path.extend(traversal_path)
    cost += traversal_cost

    return path, cost


#  Data
cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Mekelle': [('Gondar', 300)],
}

start_city = 'Addis Ababa'
strategy = 'bfs'  # Choose 'bfs' or 'dfs'

path, cost = traverse_all_cities(cities, roads, start_city, strategy)
print(f"{strategy.upper()} Path: {path} with cost {cost}")
