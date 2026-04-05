'''
.: 비어있는곳 (물 O, 고슴도치 O)
*: 물 (물 O, 고슴도치 X)
X: 돌 (물 X, 고슴도치 X)
D: 비버의 굴 (물 X, 고슴도치 O)
S: 고슴도치 위치 (물 O, 고슴도치 O)
'''

# 9:30 ~
import sys 
from collections import deque
r, c = map(int, sys.stdin.readline().split())
visited = [[False] * c for _ in range(r)]
visitedW = [[False] * c for _ in range(r)]
graph = []
S = None # 2) 좌표 사용 시 튜플 처음 선언
D = None
water = deque()

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for i in range(r):
    l = list(map(str, sys.stdin.readline().strip())) # 1) split: 공백기준 / strip: 문자열 양쪽 공백 제거
    for j, s in enumerate(l):
        if s == 'S':
            S = (i, j)
        elif s == 'D':
            D = (i, j)
        elif s == '*':
            water.append((i, j))
    graph.append(l)


def water_spread():
    global water
    size = len(water)

    for i in range(size):
        # print(water)
        wy, wx = water.popleft()

        for j in range(4):
            ny = wy + dy[j]
            nx = wx + dx[j]

            if 0 <= ny < r and 0 <= nx < c:
                if visitedW[ny][nx] == False:
                    visitedW[ny][nx] = True

                    if graph[ny][nx] == ".":
                        water.append((ny, nx))
                        graph[ny][nx] = "*"
                 
        
def bfs():
    global r, c, S

    is_possible = False
    queue = deque()
    cnt = 1
    queue.append((S[0], S[1], cnt))
    last = 0
    while queue:
        y, x, cnt = queue.popleft()

        if last != cnt:
            last = cnt
            water_spread() # 물 먼저 확장

        

        # print(y, x, cnt)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
    
            if 0 <= ny < r and 0 <= nx < c:
                if visited[ny][nx] == False:
                    visited[ny][nx] = True
                    # print("고슴도치", ny, nx)
                    if graph[ny][nx] == ".":
                        queue.append((ny, nx, cnt + 1))
                    elif graph[ny][nx] == "D":
                        is_possible = True
                        print(cnt)

        # for ii in range(len(graph)):
        #     print(graph[ii])    
        # print()
    # print(cnt)
    if is_possible == False:
        print("KAKTUS")
        return
        


bfs()

      

