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

def section_BA():
    f = open('/storage/emulated/0/Code/dataset.txt', 'r')


    N, M = map(int, f.readline().strip().split())

    students = [f.readline().strip() for _ in range(N)]

    adj = {i: [] for i in range(len(students))}

    for i in range(M):
        u, v, w = map(int, f.readline().strip().split())
        adj[u].append([v, w])


    f.close()


    def hash(word):
        num = 0
        order = 1
        for char in word:
            num += ord(char)*order
            order *= 10

        return num


    def rabin_karp(text, pattern):
        pattern_hash = hash(pattern)
        substring_hash = hash(text[:len(pattern)])

        for i in range(len(text)-len(pattern)):
            if pattern_hash == substring_hash:
                return True

            substring_hash -= ord(text[i])
            substring_hash /= 10
            substring_hash += ord(text[i+len(pattern)]) * (10**(len(pattern)-1))

        return False


    print(len(students))

    snitches = set()

    for id, name in enumerate(students):
        if rabin_karp(name, 'na') == True:
            snitches.add(id)

    print('\nsnitches:', snitches)


    src = 16


    def djikstra(src):
        minheap = [[0, src]]
        shortest = {}
        parent = {src: None}

        while minheap:
            w1, n1 = heapq.heappop(minheap)

            if n1 in shortest or n1 in snitches:
                continue

            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 in shortest or n2 in snitches:
                    continue
                heapq.heappush(minheap, [w1+w2, n2])

                if n2 not in parent:
                    parent[n2] = n1

        return shortest, parent


    x, y = djikstra(src)
    print('\nNodes who has sp:', sorted(x.keys()))


    def get_path(node, parent):

        path = []

        while node is not None:
            path.append(students[node])
            node = parent[node]

        return path[::-1]


    node = 22
    if node in y:
        print('\n', get_path(node, y))
    else:
        print(f"\nNo path to node {node}")


def solve_airport_problem_with_kruskal(n, edges, airport_cost):
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

    min_cost = float('inf')
    best_airports = 0

    # Try different numbers of airports (1 to n)
    for num_airports in range(1, n + 1):
        # Cost of building airports
        total_cost = num_airports * airport_cost

        # We need to connect nodes into exactly num_airports components
        # This means we need to build (n - num_airports) roads
        roads_needed = n - num_airports

        if roads_needed == 0:
            # All locations have airports
            if total_cost < min_cost or (total_cost == min_cost and num_airports > best_airports):
                min_cost = total_cost
                best_airports = num_airports
            continue

        # Sort edges by cost (using your approach)
        edges.sort(key=lambda x: x[2])

        # Initialize parent and rank for union-find
        parent = {i: i for i in range(1, n + 1)}
        rank = {i: 0 for i in range(1, n + 1)}

        roads_built = 0
        road_cost = 0

        # Build roads using Kruskal's algorithm
        for u, v, w in edges:
            if roads_built >= roads_needed:
                break
            if union(parent, rank, u, v) == True:
                road_cost += w
                roads_built += 1

        # Check if we can build exactly the roads we need
        if roads_built == roads_needed:
            total_cost += road_cost
            if total_cost < min_cost or (total_cost == min_cost and num_airports > best_airports):
                min_cost = total_cost
                best_airports = num_airports

    return min_cost, best_airports


def solve_test_cases():
    t = int(input("Enter number of test cases: "))

    for case_num in range(1, t + 1):
        n, m, airport_cost = map(int, input().split())

        edges = []
        for _ in range(m):
            x, y, cost = map(int, input().split())
            edges.append((x, y, cost))

        min_cost, num_airports = solve_airport_problem_with_kruskal(
            n, edges, airport_cost)
        print(f"Case #{case_num}: {min_cost} {num_airports}")

# Test with sample data


def test_samples():
    print("Testing Sample Cases:")

    # Test case 1
    print("\nTest Case 1:")
    n, m, airport_cost = 4, 4, 100
    edges = [(1, 2, 10), (4, 3, 12), (4, 1, 41), (2, 3, 23)]
    min_cost, num_airports = solve_airport_problem_with_kruskal(
        n, edges, airport_cost)
    print(f"Result: {min_cost} {num_airports}")
    print("Expected: 145 1")

    # Test case 2
    print("\nTest Case 2:")
    n, m, airport_cost = 5, 3, 1000
    edges = [(1, 2, 20), (4, 5, 40), (3, 2, 30)]
    min_cost, num_airports = solve_airport_problem_with_kruskal(
        n, edges, airport_cost)
    print(f"Result: {min_cost} {num_airports}")
    print("Expected: 2090 2")


def solve_byteland_lighting():
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
        return False

    while True:
        m, n = map(int, input().split())
        if m == 0 and n == 0:
            break

        edges = []
        total_length = 0

        for _ in range(n):
            x, y, z = map(int, input().split())
            edges.append((z, x, y))
            total_length += z

        edges.sort(key=lambda x: x[0])

        parent = {i: i for i in range(m)}
        rank = {i: 0 for i in range(m)}

        mst_length = 0
        edges_used = 0

        for weight, u, v in edges:
            if edges_used >= m - 1:
                break
            if union(parent, rank, u, v):
                mst_length += weight
                edges_used += 1

        max_savings = total_length - mst_length
        print(max_savings)


# Call this function to solve the problem
solve_byteland_lighting()

# Run the test
# test_samples()
# prim()
# kruskal()
# djikstra()
# bellman_ford()
# naive_matching()
# rabin_karp()