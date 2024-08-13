import sys 
N, M = map(int, sys.stdin.readline().split())
graph = []
parent = [0] * (N + 1)

for _ in range(M):
    v1, v2, w = map(int, sys.stdin.readline().split())
    graph.append((w, v1, v2))
graph.sort()
# print(graph)

def init(n):
    for i in range(1, n + 1):
        parent[i] = i 


def find(i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return i


def in_the_same_set(p, q):
    return find(p) == find(q)


def union(p, q):
    i = find(p)
    j = find(q)

    if i != j:
        parent[i] = j


def kruskal():
    global N, M, graph, parent

    init(N)
    ans = []
        
    for weight, u, v in graph:
        i = find(u)
        j = find(v)

        if not in_the_same_set(i, j):
            union(i, j)

            ans.append(weight)
    
    print(sum(ans[:-1]))

kruskal()
           