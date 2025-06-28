from random import *

n = 200 #number of nodes
p = 0.2 #probability of edge creation
minEdgeWeight = 1 #minimum edge weight
maxEdgeWeight = 100 #maximum edge weight

def dfs(node, n, edges):
    visited = [False] * n
    stack = [node]
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            for edge in edges:
                if edge[0] == current and not visited[edge[1]]:
                    stack.append(edge[1])
                elif edge[1] == current and not visited[edge[0]]:
                    stack.append(edge[0])
    return all(visited)

# # Create a random graph
# edges = []
# connected = False
# while not connected:
#     for i in range(n):
#         for j in range(i + 1, n):
#             if random() < p:
#                 edges.append((i, j, randint(minEdgeWeight, maxEdgeWeight)))
#     # Check if the graph is connected
#     connected = dfs(0, n, edges)
    
# # Shuffle the edges to create a random order
# shuffle(edges)
# # Write the sparse graph to a file
# with open("sparseGraph.txt", "w") as f:
#     f.write(f"{n} {len(edges)}\n")
#     for edge in edges:
#         f.write(f"{edge[0]} {edge[1]} {edge[2]}\n")
        
# Write the dense graph to a file
# with open("denseGraph.txt", "w") as f:
#     f.write(f"{n} {len(edges)}\n")
#     for edge in edges:
#         f.write(f"{edge[0]} {edge[1]} {edge[2]}\n")


def generate_graph(n, p, minEdgeWeight, maxEdgeWeight):
    edges = []
    connected = False
    while not connected:
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                if random() < p:
                    edges.append((i, j, randint(minEdgeWeight, maxEdgeWeight)))
        # Check if the graph is connected
        connected = dfs(0, n, edges)
    return edges


def create_graph_files(n, sparse_p, dense_p):
    # Generate sparse graph
    sparse_edges = generate_graph(n, sparse_p, 1, 100)
    with open(f"sparse_{n}.txt", "w") as f:
        f.write(f"{n} {len(sparse_edges)}\n")
        for edge in sparse_edges:
            f.write(f"{edge[0]} {edge[1]} {edge[2]}\n")

    # Generate dense graph
    dense_edges = generate_graph(n, dense_p, 1, 100)
    with open(f"dense_{n}.txt", "w") as f:
        f.write(f"{n} {len(dense_edges)}\n")
        for edge in dense_edges:
            f.write(f"{edge[0]} {edge[1]} {edge[2]}\n")


# Generate graphs for different sizes
create_graph_files(10, 0.2, 0.8)    # 10 nodes
create_graph_files(100, 0.1, 0.6)   # 100 nodes
create_graph_files(1000, 0.01, 0.3)  # 1000 nodes
