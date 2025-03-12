import heapq
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque
import matplotlib

matplotlib.use('TkAgg')


def bfs(start, adj):
    visited = {node: False for node in adj}
    steps = []
    q = deque([start])
    visited[start] = True
    while q:
        node = q.popleft()
        steps.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)

    return steps


def visualize(s, t, g, pos, h_values):
    adj = {node: list(g.neighbors(node)) for node in g.nodes}
    steps = bfs(s, adj)

    fig, ax = plt.subplots()

    visited_nodes = set()

    def update(node):
        ax.clear()
        visited_nodes.add(node)

        node_colors = ['r' if n in visited_nodes else 'g' for n in g.nodes]
        nx.draw(g, pos, with_labels=True, node_color=node_colors, ax=ax)

        for node_key, (x, y) in pos.items():
            ax.text(x, y + 0.25, f"h={h_values[node_key]}", fontsize=12, ha='center')

        ax.set_title(f"Visiting Node: {node}",pad=20)

    animation = FuncAnimation(fig, update, frames=steps, interval=1000, repeat=False)
    plt.show()


g = nx.DiGraph()
g.add_weighted_edges_from([
    ('S', 'A', 3), ('S', 'B', 1),
    ('A', 'C', 1), ('A', 'D', 3), ('A', 'G', 4),
    ('B', 'C', 4),
    ('C', 'G', 3),
    ('D', 'G', 2)
])

pos = {
    'S': (0, 2),
    'B': (1, 3),
    'A': (1, 1),
    'C': (2, 3),
    'D': (2, 1),
    'G': (3, 2)
}

h_values = {
    'S': 6,
    'A': 3,
    'B': 4,
    'C': 2,
    'D': 2,
    'G': 0
}

visualize('S', 'G', g, pos, h_values)
