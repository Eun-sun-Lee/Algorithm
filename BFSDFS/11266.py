import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한 증가
cnt = 0

def dfs(u, p):
    global cnt
    cnt += 1
    dfsNumber[u] = back[u] = cnt
    child = 0

    for v in graph[u]:
        if p == v:
            continue
        if dfsNumber[v] == 0:
            child += 1
            dfs(v, u)
            if (p != -1 and back[v] >= dfsNumber[u]) or (p == -1 and child > 1):
                if u not in articulPoint:
                    articulPoint.append(u)
            back[u] = min(back[u], back[v])  
        else:
            back[u] = min(back[u], dfsNumber[v])

node, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(node + 1)]
for _ in range(e):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
articulPoint = []
dfsNumber = [0] * (node + 1)
back = [0] * (node + 1)
for j in range(1, node + 1):
    if dfsNumber[j] == 0:
        dfs(j, -1)
articulPoint.sort()
print(len(articulPoint))
print(*articulPoint)