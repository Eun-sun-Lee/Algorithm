# DFS
# visited 초기화 주의 

import sys 
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())

graph = [[] * (n + 1) for _ in range(n + 1)] 
visited = [-1] * (n + 1)
for _ in range(n - 1):
    p, c, w = map(int, sys.stdin.readline().split())
    graph[p].append((c, w))
    graph[c].append((p, w))


def dfs(x, valSum):
    for i, w in graph[x]:
        if visited[i] == -1: 
            visited[i] = valSum + w # 방문 체크 
            dfs(i, valSum + w)

visited[1] = 0 # 루트 거리는 1로 초기화 
dfs(1, 0)
maxVal = max(visited)
maxIdx = visited.index(maxVal)

visited = [-1] * (n + 1)
visited[maxIdx] = 0
dfs(maxIdx, 0)
print(max(visited))
