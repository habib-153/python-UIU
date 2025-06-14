# from heapq import heappop, heappush
# import networkx as nx
# import matplotlib.pyplot as plt

# def prim(adjList, root):
#     key = [float('inf') for _ in range(len(adjList))]
#     parent = [-1 for _ in range(len(adjList))]
#     tree = [False for _ in range(len(adjList))]  
#     key[root] = 0
#     pq = [(0, root)]  # (key, vertex)
#     while pq:
#         k, u = heappop(pq)
#         if tree[u]:
#             continue
#         tree[u] = True
#         for v, w in adjList[u]:
#             if not tree[v] and w < key[v]:
#                 key[v] = w
#                 parent[v] = u
#                 heappush(pq, (w, v))
#     return key, parent

# with open('sparseGraph.txt', 'r') as f:
#     n, m = map(int, f.readline().split())
#     adjList = {i: [] for i in range(n)}
#     for _ in range(m):
#         u, v, w = map(int, f.readline().split())
#         adjList[u].append((v, w))
#         adjList[v].append((u, w))
        
# key, parent = prim(adjList, 0)

# print(f"MST total weight {sum(key)}")

# G = nx.Graph()
# for u in range(n):
#     if parent[u] != -1:
#         G.add_edge(parent[u], u, weight=key[u])
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, node_size=10, node_color='lightblue', font_size=10)
# edge_labels = nx.get_edge_attributes(G, 'weight')
# # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
# plt.show()
        

import time
from heapq import heappop, heappush


def prim(adjList, n):
    start_time = time.time()

    key = [float('inf')] * n
    parent = [-1] * n
    tree = [False] * n
    key[0] = 0
    pq = [(0, 0)]

    while pq:
        k, u = heappop(pq)
        if tree[u]:
            continue
        tree[u] = True
        for v, w in adjList[u]:
            if not tree[v] and w < key[v]:
                key[v] = w
                parent[v] = u
                heappush(pq, (w, v))

    execution_time = (time.time() - start_time) * \
        1000  # Convert to milliseconds
    return sum(key), execution_time


def kruskal(edgeList, n):
    start_time = time.time()

    parent = list(range(n))
    rank = [0] * n

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(x, y):
        px, py = find(x), find(y)
        if rank[px] < rank[py]:
            parent[px] = py
        elif rank[px] > rank[py]:
            parent[py] = px
        else:
            parent[py] = px
            rank[px] += 1

    edgeList.sort()
    total_weight = 0

    for w, u, v in edgeList:
        if find(u) != find(v):
            union(u, v)
            total_weight += w

    execution_time = (time.time() - start_time) * \
        1000  # Convert to milliseconds
    return total_weight, execution_time


def test_graph(filename):
    with open(filename, 'r') as f:
        n, m = map(int, f.readline().split())
        edges = []
        adjList = [[] for _ in range(n)]

        for _ in range(m):
            u, v, w = map(int, f.readline().split())
            edges.append((w, u, v))
            adjList[u].append((v, w))
            adjList[v].append((u, w))

    prim_weight, prim_time = prim(adjList, n)
    kruskal_weight, kruskal_time = kruskal(edges, n)

    return prim_time, kruskal_time


# Test all graph sizes
sizes = [10, 100, 1000]
print("N\tPrim\t\tKruskal")
print("-" * 40)

for n in sizes:
    # Test sparse graph
    p_time_sparse, k_time_sparse = test_graph(f"sparse_{n}.txt")
    print(f"{n} (Sparse)\t{p_time_sparse:.2f}ms\t{k_time_sparse:.2f}ms")

    # Test dense graph
    p_time_dense, k_time_dense = test_graph(f"dense_{n}.txt")
    print(f"{n} (Dense)\t{p_time_dense:.2f}ms\t{k_time_dense:.2f}ms")
