import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib

matplotlib.use('TkAgg')


def a_star_visualized(start, goal, graph, h_values, pos):
    try:
        path = nx.astar_path(graph, start, goal, heuristic=lambda n, _: h_values[n])
    except nx.NetworkXNoPath:
        print("No path found!")
        return None

    fig, ax = plt.subplots(figsize=(8, 6))
    visited = set()

    def update(frame):
        ax.clear()
        visited.add(path[frame])
        draw_graph(graph, pos, path[:frame + 1], visited, ax)

    ani = FuncAnimation(fig, update, frames=len(path), repeat=False, interval=1000)
    plt.show()

    return path


def draw_graph(g, pos, path, visited, ax):
    node_colors = ['r' if n in path else ('gray' if n in visited else 'g') for n in g.nodes]

    edge_labels = {(u, v): f"{g[u][v]['weight']}" for u, v in g.edges}

    edge_colors = ['b' if (u, v) in zip(path, path[1:]) else 'black' for u, v in g.edges]

    nx.draw(g, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, edge_cmap=plt.cm.Reds,
            node_size=1000, font_size=10, ax=ax)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_size=10, ax=ax)

    for node_key, (x, y) in pos.items():
        ax.text(x, y + 0.25, f"h={h_values[node_key]}", fontsize=12, ha='center')


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
