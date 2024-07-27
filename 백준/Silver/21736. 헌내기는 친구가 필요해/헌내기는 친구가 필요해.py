import sys 
from collections import deque 
r, c = map(int, sys.stdin.readline().split())
graph = []
start = deque()
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
visited = [[False] * c for _ in range(r)]
way = 0


for i in range(r):
    l = list(sys.stdin.readline().strip())
    for j in range(c):
        if l[j] == "I":
            start.append((i, j))
    graph.append(l)


def bfs(graph, start):
    global visited, dy, dx
    cnt = 0

    while start:
        rr, cc = start.popleft()
        # print(rr, cc)

        visited[rr][cc] = True

        for i in range(4):
            ny = dy[i] + rr 
            nx = dx[i] + cc 
            
            if 0 <= ny < r and 0 <= nx < c:

                if visited[ny][nx] == True: continue 
                visited[ny][nx] = True # 시간초과 방지 
                if graph[ny][nx] == "X":
                    continue
                elif graph[ny][nx] == "O":
                    start.append((ny, nx))
                elif graph[ny][nx] == "P":
                    start.append((ny, nx))
                    cnt += 1
    return cnt

people = bfs(graph, start)
print("TT" if people == 0 else people)

# OPP
# OIX
# PXX