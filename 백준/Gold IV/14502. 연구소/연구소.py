import sys
import copy
from collections import deque

n, m = map(int, sys.stdin.readline().split())
queue = deque()
graph = []
answer = 0
ny = [0, -1, 0, 1]
nx = [1, 0, -1, 0]

for i in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if l[j] == 2:
            queue.append((i, j))
    graph.append(l)

def makeWall(start, cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(start, n * m): # 2차원 배열 -> 1차원 배열로 변경하여 조합
        r = i // m
        c = i % m

        if graph[r][c] == 0:
            graph[r][c] = 1
            makeWall(i + 1, cnt + 1)
            graph[r][c] = 0

def bfs(): 
    graph2 = copy.deepcopy(graph)
    virus = copy.deepcopy(queue) 
    # virus = deque()
    # for i in range(n):
    #      for j in range(m):
    #          if graph2[i][j] == 2:
    #              virus.append((i, j))

    while virus:
        y, x = virus.popleft()

        for i in range(4):
            nextY = y + ny[i]
            nextX = x + nx[i]

            if 0 <= nextY < n and 0 <= nextX < m:

                if graph2[nextY][nextX] == 0:
                    graph2[nextY][nextX] = 2
                    virus.append((nextY, nextX))
    count(graph2)

def count(graph2):
    global answer
    answer = max(answer, sum(i.count(0) for i in graph2))
         
makeWall(0, 0)
print(answer)