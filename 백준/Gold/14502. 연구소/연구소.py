import sys
import copy
from collections import deque

n, m = map(int, sys.stdin.readline().split())
queue = deque()
graph = []
answer = 0

for i in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if l[j] == 2:
            queue.append((i, j))
    graph.append(l)

def makeWall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt + 1)
                graph[i][j] = 0

def bfs(): # virus 매개변수로 받아와야 나중에 queue에서 뺄 때 전역변수에 영향 X
    ny = [0, -1, 0, 1]
    nx = [1, 0, -1, 0]
    graph2 = copy.deepcopy(graph)
    virus = copy.deepcopy(queue) # # 매번 bfs 돌릴 때마다 queue에 넣고 빼므로
    visited = [[False] * m for _ in range(n)]

    while virus:
        y, x = virus.popleft()
        visited[y][x] = True # 매번 bfs 돌릴 때마다 visited 초기화 필요

        for i in range(4):
            nextY = y + ny[i]
            nextX = x + nx[i]

            if 0 <= nextY < n and 0 <= nextX < m and visited[nextY][nextX] == False:

                if graph2[nextY][nextX] == 2 or graph2[nextY][nextX] == 1: continue

                visited[nextY][nextX] = True

                if graph2[nextY][nextX] == 0:
                    graph2[nextY][nextX] = 2
                    virus.append((nextY, nextX))
    count(graph2)

def count(graph2):
    global answer
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph2[i][j] == 0: cnt += 1
    answer = max(answer, cnt)
                
makeWall(0)
print(answer)