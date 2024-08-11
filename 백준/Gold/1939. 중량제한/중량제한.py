import sys 
import heapq 

N, M = map(int, sys.stdin.readline().split())
graph = []
parent = [0] * (N + 1)

for _ in range(M):
    v1, v2, w = map(int, sys.stdin.readline().split())
    graph.append((-w, v1, v2))
start, end = map(int, sys.stdin.readline().split())
graph.sort()

def init(N):
    for i in range(1, N + 1):
        parent[i] = i 

def find(i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return i

def in_same_set(p, q):
    return find(p) == find(q)

def union(p, q):
    i = find(p)
    j = find(q)

    if i != j:
        # parent[max(i, j)] = min(i, j) # 오른쪽이 부모
        parent[i] = j

def kruskal(N, M, graph, start, end):
    global parnet 
    init(N)
    

    for w, v1, v2 in graph:
        p = find(v1)
        q = find(v2)

        if in_same_set(p, q) == False:
            union(p, q)
            
            if in_same_set(start, end):
                print(-w)
                return

kruskal(N, M, graph, start, end)
    


