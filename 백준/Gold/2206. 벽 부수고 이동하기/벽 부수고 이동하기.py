# 벽 부수고 이동하기 (골드 3) / BFS
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
# visited = [[0] * m for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)]for _ in range(n)]
for i in range(n):
    l = list(sys.stdin.readline().strip())
    for j in l:
        graph[i].append(int(j))
# print(visited)

# for i in range(n):
#     print(visited[i])
    
def bfs(startY, startX, n, m, wallLeft):
    queue = deque()
    queue.append((startY, startX, wallLeft))
    visited[startY][startX][wallLeft] = 1
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    while queue:
        y, x, wallLeft = queue.popleft()
        if y == n - 1 and x == m - 1 : return visited[y][x][wallLeft]

        for i in range(4):
            nextY = dy[i] + y
            nextX = dx[i] + x

            if 0 <= nextX < m and 0 <= nextY < n:
                if visited[nextY][nextX][wallLeft] != 0: continue
                if graph[nextY][nextX] == 0:
                    visited[nextY][nextX][wallLeft] = visited[y][x][wallLeft] + 1
                    queue.append((nextY, nextX, wallLeft))
                else:
                    if wallLeft == 1:
                        visited[nextY][nextX][wallLeft - 1] = visited[y][x][wallLeft] + 1
                        queue.append((nextY, nextX, wallLeft - 1))
    return -1

print(bfs(0, 0, n, m, 1))