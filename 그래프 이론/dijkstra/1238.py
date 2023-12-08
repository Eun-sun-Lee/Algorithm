import sys
import heapq

n, m, dst = map(int,sys.stdin.readline().split())

def dijkstra(n, idx, dst, graph):
    D = [1000001] * (n + 1)
    prev = [0] * (n + 1)
    heap = [(0, 1)]
    for node, weight in graph[idx]:
        heapq.heappush(heap, (weight, node)) # heap에 넣을 땐 정렬할 값(weight)을 앞으로
        D[node] = weight
        prev[node] = idx
    while heap:
        curr_dist, u = heapq.heappop(heap)
        if D[u] < curr_dist: continue
        for v, weight in graph[u]:
            if D[u] + weight < D[v]:
                D[v] = D[u] + weight
                prev[v] = u
                heapq.heappush(heap, (weight, v))
    return D

graph = [[] for _ in range(n + 1)]
goCome = [0] * (n + 1)
for _ in range(m):
    v1, v2, w = map(int,sys.stdin.readline().split())
    graph[v1].append((v2, w)) # v2, weight
for num in range(1, n + 1):
    if num == dst: continue
    go = dijkstra(n, num, dst, graph)
    goCome[num] = go[dst]
# print(goCome)
come = dijkstra(n, dst, dst, graph)

ans = [a + b for a, b in zip(goCome, come)]
# print(ans)
# print(come)
ans[0] = -1
print(max(ans))



