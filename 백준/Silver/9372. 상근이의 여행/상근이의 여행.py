import heapq 
import sys

t = int(input())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    answer = 0

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # print(graph)

    def prim(start):
        global answer
        heap = []
        heapq.heappush(heap, start)
        visited[start] = True

        while heap:
            if all(visited):
                print(answer)
                return 

            node = heapq.heappop(heap)
            visited[node] = True
            

            for next in graph[node]:
                if visited[next] == False:
                    answer += 1
                    visited[next] = True 
                    heapq.heappush(heap, next)
            # if node == m:
                # print(answer)
    prim(1)

    print(answer)


