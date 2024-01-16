import sys
from collections import deque
c, r = map(int, sys.stdin.readline().split())
graph = []
visited = [[False] * c for _ in range(r)]
start = deque()
for i in range(r):
    l = list(map(int, sys.stdin.readline().split()))
    graph.append(l)
    for j in range(c):
        if l[j] == 1: start.append((j, i, 0))

    def bfs(queue):
        global c, r, cnt
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        while queue:
            # print(queue)
            x, y, day = queue.popleft()
            visited[y][x] = True
            count = day
            for i in range(4):
                nextX = x + dx[i]
                nextY = y + dy[i]

                if nextX >= 0 and nextX < c and nextY >= 0 and nextY < r:
                    if visited[nextY][nextX] == True: continue
                    if graph[nextY][nextX] == -1:
                        visited[nextY][nextX] = True 
                        continue # 갈 수 없음.
                    # if (nextX,nextY,day) in queue: break 시간초과
                    queue.append((nextX, nextY, count + 1))
                    visited[nextY][nextX] = True 
        return count
if len(start) == r*c:
    count = 0
elif len(start) != 0:
    count = bfs(start)
    for i in range(r):
        for j in range(c):
            if visited[i][j] == False and graph[i][j] != -1: # 토마토가 모두 익지 못하는 상황
                count = -1
                break
else:
    count = -1
# print(visited)
print(count)