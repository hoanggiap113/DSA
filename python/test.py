import heapq


def dijkstra(s, n, adj):
    # Khởi tạo khoảng cách với giá trị vô cùng
    INF = float('inf')
    d = [INF] * (n + 1)
    d[s] = 0

    # Hàng đợi ưu tiên (khoảng cách, đỉnh)
    Q = []
    heapq.heappush(Q, (0, s))

    while Q:
        # Chọn đỉnh có khoảng cách từ s nhỏ nhất
        kc, u = heapq.heappop(Q)

        # Nếu khoảng cách hiện tại lớn hơn khoảng cách đã lưu, bỏ qua
        if kc > d[u]:
            continue

        # Relaxation: Cập nhật khoảng cách từ s tới các đỉnh kề với u
        for v, w in adj[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                heapq.heappush(Q, (d[v], v))

    return d


# Ví dụ sử dụng
n = 4  # Số đỉnh
adj = {
    1: [(2, 1), (4, 4)],
    2: [(1, 1), (3, 2), (4, 3)],
    3: [(2, 2)],
    4: [(1, 4), (2, 3)]
}

s = 1  # Đỉnh nguồn
distances = dijkstra(s, n, adj)
print("Khoảng cách từ đỉnh", s, "đến các đỉnh khác:", distances[1:])