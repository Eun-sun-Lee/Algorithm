# 최단경로 (골드 4)
import sys
import heapq
node,e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(node + 1)]
for _ in range(e):
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append((v,w))

def dijkstra(start, graph):
    heap = [(0, start)]
    distance = [100000001] * (node + 1)
    distance[start] = 0 # 시작할 때 필요, 주의

    while heap:
        curr_dist, u = heapq.heappop(heap)
        if distance[u] < curr_dist: continue
        for v, weight in graph[u]:
            if distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                heapq.heappush(heap, (distance[v], v))
    return distance
distance = dijkstra(start, graph)
for i in range(1, node + 1):
    if distance[i] == 100000001: print("INF")
    else: print(distance[i])
    

