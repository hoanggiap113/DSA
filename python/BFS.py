import heapq
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque
import matplotlib

matplotlib.use('TkAgg')

def bfs(start, goal, adj):
    visited = {node: False for node in adj}
    parent = {node: None for node in adj}  # To keep track of the path
    q = deque([start])
    visited[start] = True
    visited_edges = set()  # To keep track of visited edges

    while q:
        node = q.popleft()

        # If we reach the goal, reconstruct the path
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path, visited_edges  # Return both path and visited edges

        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node  # Record the parent of the neighbor
                q.append(neighbor)
                visited_edges.add((node, neighbor))  # Add the edge to visited edges

    return [], visited_edges  # Return empty path and visited edges if no path is found

def visualize(s, t, g, pos, h_values):
    adj = {node: list(g.neighbors(node)) for node in g.nodes}
    steps, visited_edges = bfs(s, t, adj)  # Get both path and visited edges

    fig, ax = plt.subplots()

    visited_nodes = set()
    visited_edges_set = set()  # To keep track of edges to be colored

    def update(node):
        ax.clear()
        visited_nodes.add(node)

        # Update visited edges
        if len(visited_nodes) > 1:
            previous_node = steps[steps.index(node) - 1]
            visited_edges_set.add((previous_node, node))

        node_colors = ['r' if n in visited_nodes else 'g' for n in g.nodes]
        edge_colors = ['b' if (u, v) in visited_edges_set or (v, u) in visited_edges_set else 'k' for u, v in g.edges]
        edge_widths = [3 if (u, v) in visited_edges_set or (v, u) in visited_edges_set else 1 for u, v in g.edges]

        nx.draw(g, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, width=edge_widths, ax=ax)

        for node_key, (x, y) in pos.items():
            ax.text(x, y + 0.25, f"h={h_values[node_key]}", fontsize=12, ha='center')

        ax.set_title(f"Visiting Node: {node}", pad=20)

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