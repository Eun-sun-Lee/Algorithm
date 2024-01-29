import sys
from collections import deque

n = int(sys.stdin.readline())
graph = []
visited = [[False] * n for _ in range(n)]
startX = 0
startY = 0
cntTotal = 0
sharkSize = 2
sharkCnt = 0

for i in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    graph.append(l)

    for j in range(n):
        if l[j] == 9:
            startY = i
            startX = j

def bfs(graph, startY, startX):
    global cntTotal, sharkSize, sharkCnt
    visited = [[False] * n for _ in range(n)]

    # dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    queue = deque()
    queue.append((0, startY, startX))  # Change initial count to 0
    # visited[startY][startX] = True
    eat = sys.maxsize, startY, startX

    while queue:
        cnt, y, x = queue.popleft()

        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]

            if 0 <= nextX < n and 0 <= nextY < n:
                if graph[nextY][nextX] > sharkSize or visited[nextY][nextX]: continue
                if 0 < graph[nextY][nextX] < sharkSize:

                    eat = min(eat, (cnt + 1, nextY, nextX))

                visited[nextY][nextX] = True
                queue.append((cnt + 1, nextY, nextX))

    return eat

 # 이거 때메 자꾸 값 이상함 (맨처음 시작점-9도 graph 값 초기화 필요)
while True:
    graph[startY][startX] = 0
    count, startY, startX = bfs(graph, startY, startX)
    if count == sys.maxsize:
        break
    sharkCnt += 1
    cntTotal += count

    if sharkCnt == sharkSize:
        sharkSize += 1
        sharkCnt = 0

print(cntTotal)
