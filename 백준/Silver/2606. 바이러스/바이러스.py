from collections import deque

v = int(input())
e = int(input())
graph = [[] for _ in range(v+1)]
# print(graph)
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) 
# print(graph)

def bfs(x):
    deq = deque([x])
    count = 0
    visited[x] = True
    while deq:
        node = deq.popleft()
        for n in graph[node]:
            if not visited[n]:
                visited[n] = True
                deq.append(n)
                count += 1
    return count

visited = [False for _ in range(v+1)]
print(bfs(1))