import sys

count = 0
v = int(sys.stdin.readline())
e = int(sys.stdin.readline())
graph = [[] for _ in range(v + 1)]
visited = [False for _ in range(v + 1)]
for _ in range(e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
# print(graph)
visited = [False for _ in range(v + 1)]
def dfs(x, count):
    visited[x] = True
    for i in graph[x]:
        if visited[i] == False:
            count = dfs(i, count + 1)
    return count

print(dfs(1, count))

#[[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]