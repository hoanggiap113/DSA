import queue
import networkx as nx
import matplotlib.pyplot as plt
import time

def bfs(g,u):
    visited = set()
    q = queue.Queue()
    q.put(u)
    order = []
    while not q.empty():
        v = q.get()
        if v not in visited:
            order.append(v)
            visited.add(v)
            for node in g[v]:
                if node not in visited:
                    q.put(node)
    return order
def visualize(order,title,g,pos):
    plt.figure()
    plt.title(title)
    for i, node in enumerate(order):
        plt.clf()
        plt.title(title)
        nx.draw(g,pos,labels={n: n for n in g.nodes},node_color=['r' if n == node else 'g' for n in g.nodes])
        plt.draw()
        plt.pause(0.5)
    plt.show()
    time.sleep(0.5)
g = nx.Graph()
g.add_edges_from([('A','B'),('A','C'),('B','D'),('B','E'),('C','F'),('C','G')])
pos = nx.spring_layout(g)
visualize(bfs(g,'A'),"BFS visualization",g,pos)