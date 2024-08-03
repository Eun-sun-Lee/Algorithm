import sys 
from collections import deque 

V, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V + 1)]
degree = [0] * (V + 1)

for i in range(E):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    degree[v2] += 1

def topological_sort(V, E, graph, degree):
    queue = deque()
    result = []

    for i in range(1, V + 1):
        if degree[i] == 0:
            queue.append(i)
    
    while queue:
        curr = queue.popleft()
        result.append(curr)

        for j in graph[curr]:
            degree[j] -= 1

            if degree[j] == 0:
                queue.append(j)
    print(*result)
topological_sort(V, E, graph, degree)