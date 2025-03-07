import heapq
import networkx as nx
import matplotlib.pyplot as plt
import time
# n, m, s, t = map(int, input().split())
# adj = [[] for _ in range(n + 1)]
# visited = [False] * (n + 1)
# parent = [0] * (n + 1)
#
# for _ in range(m):
#     x, y = map(int, input().split())
#     adj[x].append(y)
#     adj[y].append(x)
# def dfs(u, ke, visited,order):
#     print(u, end=" ")
#     visited[u] = True
#     order.append(u)
#     for v in ke[u]:
#         if not visited[v]:
#             dfs(v, ke, visited,order)

# def bfs(u, adj, visited):
#     q = deque()
#     q.append(u)
#     visited[u] = True
#     order = []
#     while q:
#         v = q.popleft()
#         order.append(v)
#         print(v,end = " ")
#         for x in adj[v]:
#             if not visited[x]:
#                 q.append(x)
#                 visited[x] = True
#     return order

def dijkstra(s, n, adj):
    INF = float('inf')
    d = [INF] * (n + 1)
    d[s] = 0
    Q = []
    heapq.heappush(Q, (0, s))
    while Q:
        kc, u = heapq.heappop(Q)
        if kc > d[u]:
            continue
        for v, w in adj[u].items():
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                heapq.heappush(Q, (d[v], v))
    return d


def visualize(s, t, g, pos):
    adj = {node: {neighbor: g[node][neighbor]['weight'] for neighbor in g.neighbors(node)} for node in g.nodes}
    n = len(g.nodes)
    d = dijkstra(s, n, adj)

    path = []
    curr = t
    while curr != s:
        path.append(curr)
        for neighbor in g.neighbors(curr):
            if d[neighbor] + g[curr][neighbor]['weight'] == d[curr]:
                curr = neighbor
                break
    path.append(s)
    path.reverse()

    # Tạo danh sách các cạnh trên đường đi
    path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]

    # Mô phỏng đường đi từng bước
    plt.figure()
    plt.title(f"Shortest Path from {s} to {t}")

    # Khởi tạo danh sách các node và cạnh đã được tô màu
    colored_nodes = []
    colored_edges = []

    for i, node in enumerate(path):
        # Thêm node hiện tại vào danh sách đã tô màu
        colored_nodes.append(node)

        # Nếu không phải node đầu tiên, thêm cạnh từ node trước đó đến node hiện tại
        if i > 0:
            colored_edges.append((path[i - 1], path[i]))

        # Vẽ đồ thị
        plt.clf()
        plt.title(f"Shortest Path from {s} to {t}")

        # Vẽ tất cả các node
        nx.draw(g, pos, labels={n: n for n in g.nodes},
                node_color=['r' if n in colored_nodes else 'g' for n in g.nodes])

        # Vẽ trọng số trên các cạnh
        edge_labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)

        # Tô màu các cạnh đã đi qua
        nx.draw_networkx_edges(g, pos, edgelist=colored_edges, edge_color='b', width=2)

        # Hiển thị từng bước
        plt.draw()
        plt.pause(0.5)

    plt.show()
    time.sleep(0.5)


g = nx.Graph()
g.add_edges_from([(1, 2, {'weight': 3}), (1, 3, {'weight': 4}), (2, 4, {'weight': 2}),
                  (2, 5, {'weight': 3}), (3, 6, {'weight': 7}), (3, 7, {'weight': 6}),
                  (3, 5, {'weight': 1}),(6, 7, {'weight': 5}),(5, 7, {'weight': 6}),
                  (1, 5, {'weight': 10})])

pos = {
    2: (0, 2),
    1: (-1, 1),
    4: (2, 2),
    5: (1, 1),
    3: (0, 0),
    6: (3, 0),
    7: (4, 1)
}

visualize(1, 5, g, pos)

