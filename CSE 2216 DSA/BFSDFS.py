import collections

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for i in graph[start]:
        if i not in visited:
            # visited.add(i)
            dfs(graph, i, visited)
    return visited

def bfs(graph, start):
    visited, queue = set(), collections.deque([start])
    visited.add(start)
    while queue:
        vertex = str(queue.popleft())
        print(str(vertex), end=" ")
        for i in graph[vertex]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
    

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

print(dfs(graph, '0'))
print(bfs(graph, 0))


def find_max_weight_cell(exits):
    n = len(exits)
    weights = [0] * n

    for i in range(n):
        if exits[i] != -1:
            weights[exits[i]] += i

    max_weight = -1
    max_weight_cell = -1

    for i in range(n):
        if weights[i] > max_weight or (weights[i] == max_weight and i > max_weight_cell):
            max_weight = weights[i]
            max_weight_cell = i

    return max_weight_cell


# Example usage:
exits1 = [2, 0, -1, 2]
exits2 = [-1]
print(find_max_weight_cell(exits1))  # Output: 2
print(find_max_weight_cell(exits2))  # Output: 0
