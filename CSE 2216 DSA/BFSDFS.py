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