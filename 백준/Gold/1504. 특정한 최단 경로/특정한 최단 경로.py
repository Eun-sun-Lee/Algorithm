import sys
import heapq
import copy
node, edge = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(node + 1)]
visited = [[False] for _ in range(node + 1)]

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
l = [1, first, first, second, second, node]
for i in range(4):
    cnt = 0
    for j in range(3):
        j *= 2
        cnt += dijkstra(graph, l[j], l[j + 1])
        if i == 2 and j ==0:
            cnt *= 2
        elif i == 3 and j == 0:
            cnt *= 2
    answer = min(answer, cnt)
    if i == 0:
        l = [1, second, second, first, first, node]
    elif i == 1:
        l = [1, second, 1, first, first, node]
    elif i == 2:   
        l = [1, first, 1, second, second, node]     

print(-1 if answer == sys.maxsize else answer)
# dijkstra 2번
# 1->2, 2->3, 3->4
# 1->3, 3->2, 2->4

# 1->2 1->3 2->4
# 1->2 1->3 3->4