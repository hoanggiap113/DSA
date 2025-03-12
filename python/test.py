import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque

# Tạo đồ thị
G = nx.Graph()
edges = [
    ('S', 'A', 1), ('S', 'B', 2),
    ('A', 'C', 3), ('A', 'D', 4),
    ('B', 'D', 5), ('B', 'E', 6),
    ('C', 'F', 7), ('D', 'F', 8),
    ('E', 'G', 9), ('F', 'G', 10)
]
G.add_weighted_edges_from(edges)

# Khởi tạo BFS
start = 'S'
goal = 'G'
queue = deque([(start, [start])])
visited = set()


# Hàm cập nhật animation
def update(frame):
    plt.clf()
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    if queue:
        node, path = queue.popleft()
        if node == goal:
            print("Đường đi từ S đến G:", path)
            return
        if node not in visited:
            visited.add(node)
            for neighbor in G[node]:
                queue.append((neighbor, path + [neighbor]))
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='red', node_size=2000)


# Tạo animation
fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, frames=range(10), repeat=False)
plt.show()