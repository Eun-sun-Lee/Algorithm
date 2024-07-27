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
            visited[i][j] = True
    graph.append(l)


def bfs(graph, start):
    global visited, dy, dx
    cnt = 0 # 3) cnt - 전역으로 관리 

    while start:
        rr, cc = start.popleft()

        # visited[rr][cc] = True # 1) 방문 처리 

        for i in range(4):
            ny = dy[i] + rr 
            nx = dx[i] + cc 
            
            if 0 <= ny < r and 0 <= nx < c:
                if visited[ny][nx] == False:
                    visited[ny][nx] = True # 2) 방문 처리 

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