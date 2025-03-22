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

def a_star(start, goal, adj, h_values):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {node: float('inf') for node in adj}
    g_score[start] = 0
    f_score = {node: float('inf') for node in adj}
    f_score[start] = h_values[start]

    visited_edges = set()  # To keep track of visited edges

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, visited_edges  # Return both path and visited edges

        for neighbor in adj[current]:
            tentative_g_score = g_score[current] + 1  # Assuming each step has a cost of 1

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h_values[neighbor]
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
                visited_edges.add((current, neighbor))  # Add the edge to visited edges

    return [], visited_edges  # Return empty path and visited edges if no path is found

def visualize(s, t, g, pos, h_values):
    adj = {node: list(g.neighbors(node)) for node in g.nodes}
    steps, visited_edges = a_star(s, t, adj, h_values)  # Get both path and visited edges

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
        edge_colors = ['r' if (u, v) in visited_edges_set or (v, u) in visited_edges_set else 'k' for u, v in g.edges]

        nx.draw(g, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, ax=ax)

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

pos =