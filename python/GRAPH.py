import queue
from collections import deque
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
def dfs(u, ke, visited,order):
    print(u, end=" ")
    visited[u] = True
    order.append(u)
    for v in ke[u]:
        if not visited[v]:
            dfs(v, ke, visited,order)

def bfs(u, adj, visited):
    q = deque()
    q.append(u)
    visited[u] = True
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        print(v,end = " ")
        for x in adj[v]:
            if not visited[x]:
                q.append(x)
                visited[x] = True
    return order

def visualize(order, title, g, pos):
    plt.figure()
    plt.title(title)
    for i, node in enumerate(order):
        plt.clf()
        plt.title(title)
        nx.draw(g, pos, labels={n: n for n in g.nodes}, node_color=['r' if n == node else 'g' for n in g.nodes])
        plt.draw()
        plt.pause(0.5)
    plt.show()
    time.sleep(0.5)

g = nx.Graph()
g.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])

adj = {node: list(g.neighbors(node)) for node in g.nodes}
pos = nx.spring_layout(g)

# #visualize cho bfs
# visited_bfs = {node: False for node in g.nodes}
# order_bfs = bfs('A', adj, visited_bfs)
# visualize(order_bfs, "DFS visualization", g, pos)

#Visualize cho dfs
visited_dfs = {node: False for node in g.nodes}
order_dfs = []
dfs('A',g, visited_dfs, order_dfs)
visualize(order_dfs, "DFS visualization", g, pos)
