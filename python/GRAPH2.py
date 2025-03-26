import networkx as nx
import matplotlib.pyplot as plt
import time


def a_star_visualized(start, goal, graph, h_values, pos):
    try:
        path = nx.astar_path(graph, start, goal, heuristic=lambda n, _: h_values[n])
    except nx.NetworkXNoPath:
        print("No path found!")
        return None

    plt.figure(figsize=(8, 6))
    visited = set()

    for i in range(len(path)):
        visited.add(path[i])
        draw_graph(graph, pos, path[:i + 1], visited)
        time.sleep(1)

    return path


def draw_graph(g, pos, path, visited):
    plt.clf()
    node_colors = ['r' if n in path else ('gray' if n in visited else 'g') for n in g.nodes]
    nx.draw(g, pos, with_labels=True, node_color=node_colors, edge_color='black', node_size=1000, font_size=10)
    plt.title("A* Search Visualization - Step by Step")
    plt.pause(1)


G = nx.DiGraph()
G.add_weighted_edges_from([
    ('S', 'A', 3), ('S', 'F', 2),
    ('A', 'B', 1), ('A', 'E', 3),
    ('B', 'D', 3), ('B', 'C', 1),
    ('C', 'G', 2),
    ('D', 'G', 2),
    ('E', 'C', 2),
    ('F', 'B', 3),
    ('B', 'E', 1)
])

pos = {
    'S': (0, 2), 'A': (1, 1), 'F': (1, 3),
    'B': (3, 3), 'E': (3, 1), 'D': (5, 3),
    'C': (5, 1), 'G': (6, 2)
}

h_values = {'S': 6, 'A': 4, 'F': 4, 'B': 4, 'E': 3, 'D': 1, 'C': 1, 'G': 0}

a_star_visualized('S', 'G', G, h_values, pos)
