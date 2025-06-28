import heapq

#prim
def prim():
    graph = {
        'A': [('B', 1), ('C', 3)],
        'B': [('A', 1), ('C', 1), ('D', 6)],
        'C': [('A', 3), ('B', 1), ('D', 2)],
        'D': [('B', 6), ('C', 2)]
    }


    start_node = 'A'

    visited = set()

    min_heap = [(0, start_node)]
    total_cost = 0

    while min_heap:
        cost, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        total_cost += cost

        for n, edge_cost in graph[node]:
            if n not in visited:
                heapq.heappush(min_heap, (edge_cost, n))
    print(total_cost)


# kruskal
def kruskal():
    nodes = ['A', 'B', 'C', 'D']


    edges = [
        ('A', 'B', 1),
        ('A', 'C', 3),
        ('B', 'C', 1),
        ('B', 'D', 6),
        ('C', 'D', 2)
    ]

    def find_root(parent, node):
        while parent[node] != node:
            node = parent[node]
        return node

    def union(parent, rank, u, v):
        root_u = find_root(parent, u)
        root_v = find_root(parent, v)

        if root_u != root_v:
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            elif rank[root_v] > rank[root_u]:
                parent[root_u] = root_v
            else:
                parent[root_u] = root_v
                rank[root_v] += 1
            
            return True
        else:
            return False
    
    edges.sort(key=lambda x: x[2])
    
    parent = {node: node for node in nodes}
    rank = {node: 0 for node in nodes}

    total_cost = 0

    for u, v, w in edges:
        if union(parent, rank, u, v) == True:
            total_cost += w
    print(total_cost)
    return total_cost


def djikstra():
    n = 5  # nodes = 0 -> (n-1)

    edges = [[0, 1, 10],  # edge = [u,v,w]
            [0, 2, 3],
            [1, 3, 2],
            [2, 1, 4],
            [2, 3, 8],
            [2, 4, 2],
            [3, 4, 5]]
    src= 0
    adj = {}
    for i in range(n):
        adj[i] = []
    for u, v, w in edges:
        adj[u].append([w, v])
    
    print(adj)
    shortest= {}
    min_heap = [[0, src]]

    while min_heap:
        w1, v1 = heapq.heappop(min_heap)

        if v1 in shortest:
            continue
        shortest[v1] = w1

        for w2, v2 in adj[v1]:
            if v2 not in shortest:
                heapq.heappush(min_heap, [w1 + w2, v2])
    
    for i in range(n):
        if i not in shortest:
            shortest[i] = -1

    print(shortest)
    return shortest

# bellman ford
def bellman_ford():
    n = 5  # nodes = 0 -> (n-1)

    edges = [[0, 1, 10],  # edge = [u,v,w]
            [0, 2, 3],
            [1, 3, 2],
            [2, 1, 4],
            [2, 3, 8],
            [2, 4, 2],
            [3, 4, 5]]
    src= 0
    
    dst = [float("inf")] * n
    dst[src] = 0 

    for _ in range(n+1):
        for u,v,w in edges:
            if dst[u] != float("inf") and dst[u] + w < dst[v]:
                dst[v] = dst[u] + w
    
    for u, v, w in edges:
        if dst[u] != float("inf") and dst[u] + w < dst[v]:
            return "Negative weight cycle detected"
    for i in range(n):
        if dst[i] == float('inf'):
            dst[i] = -1

    return {i: dst[i] for i in range(n)}


# pattern
text = "Before was was was, was was is."
pattern = "was"

# naive pattern matching
def naive_matching():
    splitted_text = text.split()
    count = 0
    positions = []
    print(splitted_text)

    for i, word in enumerate(splitted_text):
        if pattern in word:
            count += 1
            positions.append(i)
    print(f'COunt {count}, positions {positions}')


# rabin karp
def rabin_karp():
    def str_to_hash(s):
        num = 0
        order = 1

        for i in s:
            num += ord(i) * order
            order *= 10
        return num
    
    pattern_hash = str_to_hash(pattern)
    sub_string_hash = str_to_hash(text[:len(pattern)])
    print(f"Pattern hash: {pattern_hash}, Substring hash: {sub_string_hash}")
    for i in range(len(text) - len(pattern)):
        if pattern_hash == sub_string_hash:
            print(f"Pattern found at index {i}")
        sub_string_hash -= ord(text[i])
        sub_string_hash /= 10
        sub_string_hash += ord(text[i + len(pattern)]) * (10 ** (len(pattern) - 1))

# prim()
# kruskal()
# djikstra()
# bellman_ford()
# naive_matching()
rabin_karp()