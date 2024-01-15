import sys
cnt = 1

while True:
    n, e = map(int, sys.stdin.readline().split())
    if n == 0 and e == 0: break

    graph = [[] for _ in range(n + 1)]
    parent = [0] * (n + 1)
    visited = [False for _ in range(n + 1)]
    tree = 0

    def dfs(x):
        global tree, cycle
        visited[x] = True
        for i in graph[x]:
            if parent[x] == i: continue # 방문한적 O, cycle X
            if visited[i] == True:
                cycle = True
                break
            else:
                parent[i] = x
                dfs(i)

    for _ in range(1, e + 1):
        l = list(map(int, sys.stdin.readline().split()))
        v1 = l[0]
        v2 = l[1]
        graph[v1].append(v2)
        graph[v2].append(v1)

    for i in range(1, n + 1):
        cycle = False
        if visited[i]: continue
        if len(graph[i]) != 0:
            dfs(i)
        if cycle == False:
            tree += 1

    if tree == 0:
        print(f"Case {cnt}: No trees.")
    elif tree == 1:
        print(f"Case {cnt}: There is one tree.")
    else:
        print(f"Case {cnt}: A forest of {tree} trees.")
    cnt += 1