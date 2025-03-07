import networkx as nx
import pygame
import sys

# Khởi tạo pygame
pygame.init()

# Cài đặt kích thước màn hình
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Tạo đồ thị
G = nx.Graph()

# Thêm các nút và cạnh
edges = [
    (0.5, 4), (0.1, 3), (0.2, 4), (0.3, 5), (0.6, 4),
    (0.7, 4), (0.8, 4), (0.9, 4), (0.10, 4), (0.11, 4),
    (0.12, 4), (0.13, 4), (0.14, 4), (0.15, 4), (0.16, 4),
    (0.17, 4), (0.18, 4), (0.19, 4), (0.20, 4), (0.21, 4),
    (0.22, 4), (0.23, 4), (0.24, 4)
]

G.add_edges_from(edges)

# Vị trí các nút
pos = nx.spring_layout(G)

# Màu sắc
background_color = (255, 255, 255)
node_color = (0, 0, 255)
edge_color = (0, 0, 0)
visited_color = (255, 0, 0)

# Vẽ đồ thị
def draw_graph():
    screen.fill(background_color)
    for edge in G.edges():
        pygame.draw.line(screen, edge_color, pos[edge[0]], pos[edge[1]], 2)
    for node in G.nodes():
        pygame.draw.circle(screen, node_color, (int(pos[node][0]), int(pos[node][1])), 10)
    pygame.display.flip()

# Thực hiện BFS
def bfs(start_node):
    visited = set()
    queue = [start_node]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            pygame.draw.circle(screen, visited_color, (int(pos[node][0]), int(pos[node][1])), 10)
            pygame.display.flip()
            pygame.time.wait(500)  # Đợi 0.5 giây
            queue.extend([n for n in G.neighbors(node) if n not in visited])

# Vòng lặp chính
draw_graph()
bfs(0.5)

# Chờ đóng cửa sổ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()