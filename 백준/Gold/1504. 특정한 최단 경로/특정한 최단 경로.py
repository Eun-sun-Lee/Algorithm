import heapq 
import sys 

n, m = map(int ,sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
answer = sys.maxsize

for _ in range(m):
    a, b, w = map(int, sys.stdin.readline().split())
    graph[a].append((b, w)) # (n1, w)
    graph[b].append((a, w)) # (n2, w)
n1, n2 = map(int, sys.stdin.readline().split())


def dijkstra(graph, start, end):
    distance = [sys.maxsize] * (n + 1)
    heap = [(0, start)]
    distance[start] = 0

    while heap:
        curr_dist, u = heapq.heappop(heap)

        if distance[u] < curr_dist : continue 

        for v, w in graph[u]:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w 
                heapq.heappush(heap, (distance[v], v))

    return distance[end]


dijkstra(graph, 1, n)

l = [1, n1, n2, n]
for ii in range(2):
    cnt = 0
    for jj in range(3):
        cnt += dijkstra(graph, l[jj], l[jj + 1])
    answer = min(answer, cnt)
    l = [1, n2, n1, n]

print(-1 if answer == sys.maxsize else answer)