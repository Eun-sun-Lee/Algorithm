import sys
import heapq
node, edge = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(node + 1)]

for i in range(edge):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
first, second = map(int, sys.stdin.readline().split())

def dijkstra(graph, start, end):
    heap = [(0, start)]
    distance = [sys.maxsize] * (node + 1)
    distance[start] = 0

    while heap:
        curr_dist, u = heapq.heappop(heap)
        if distance[u] < curr_dist: continue
        for v, weight in graph[u]:
            if distance[v] > distance[u] + weight:
                distance[v] = distance[u] + weight
                heapq.heappush(heap, (distance[v], v))
    return distance[end]

answer = sys.maxsize
l = [1, first, second, node]
for i in range(2):
    cnt = 0
    for j in range(3):
        cnt += dijkstra(graph, l[j], l[j + 1])
    answer = min(answer, cnt)
    l = [1, second, first, node]
   

print(-1 if answer == sys.maxsize else answer)