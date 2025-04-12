import networkx as nx
import math
#Ô trống là ô đi được còn ô có chữ "x" là ô bị chặn
grid = [
    ["", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "x", "", "", "", "", "", "", ""],
    ["", "", "", "x", "x", "x", "x", "x", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", ""]
]

rows = len(grid)
cols = len(grid[0])

# Tạo đồ thị
G = nx.Graph()

# Các hướng đi và chi phí
directions = [
    ((-1, 0), 1), ((1, 0), 1), ((0, -1), 1), ((0, 1), 1),  # Dọc ngang
    ((-1, -1), 4), ((-1, 1), 4), ((1, -1), 4), ((1, 1), 4)  # Chéo
]

# Thêm cạnh giữa các ô không bị chặn
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "x":
            continue
        for (dx, dy), cost in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] != "x":
                G.add_edge((i, j), (ni, nj), weight=cost)


# Tọa độ điểm bắt đầu và kết thúc
A = (4, 7)
B = (1, 4)

def heu(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

# Tìm đường đi bằng A*
path = nx.astar_path(G, A, B, heuristic=heu, weight='weight')

printed_grid = [["." for _ in range(cols)] for _ in range(rows)]

# Đánh dấu ô bị chặn
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "x":
            printed_grid[i][j] = "x"

# Đánh dấu đường đi bằng "o"
for (i, j) in path:
    printed_grid[i][j] = "o"

si, sj = A
gi, gj = B
printed_grid[si][sj] = "A"
printed_grid[gi][gj] = "B"

print("Ma trận với đường đi được đánh dấu (o):")
print("Đường đi được đánh dấu là o")
for row in printed_grid:
    print(" ".join(row))
