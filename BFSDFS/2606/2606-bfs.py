from collections import deque
import sys

v = int(sys.stdin.readline())
e = int(sys.stdin.readline())
graph = [[] for _ in range(v + 1)]
visited = [False for _ in range(v + 1)]
for _ in range(e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
# print(graph)
def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = True
    count = 0
    while queue:
        n = queue.popleft()
        for next in graph[n]:
            if visited[next] == False:
                visited[next] = True
                count += 1
                queue.append(next)
                print(queue)
    return count

print(bfs(1))

# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
# deque([2])
# deque([2, 5])
# deque([5, 3])
# deque([3, 6])