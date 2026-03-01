import sys

def dfs(node, parent):
    global visited
    visited[node] = True

    for nx in graph[node]:
        if visited[nx] == False:
            if dfs(nx, node) == False: # 사이클이 있다면
                return False # 바로 리턴
        else: # 이미 방문한 노드라면
            if parent != nx:
                return False
    return True 

case = 0
while True:
    case += 1
    n, m = map(int, sys.stdin.readline().split())

    if n == 0 and m == 0: break

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for _ in range(m):
        v1, v2 = map(int, sys.stdin.readline().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    answer = 0
    for i in range(1, n + 1):
        if visited[i] == False:
            if dfs(i, -1) == True:
                answer += 1
    
    if answer == 0:
        print(f"Case {case}: No trees.")
    elif answer == 1:
        print(f"Case {case}: There is one tree.")
    else:
        print(f"Case {case}: A forest of {answer} trees.")
    
