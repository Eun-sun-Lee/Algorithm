import sys
from collections import deque
a,b,c = map(int,input().split())
visit = [[0]*b for _ in range(a)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
# visit = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
for i in range(c):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2,1):
        for j in range(x1,x2,1):
            visit[i][j]=1

queue = deque()
area = []

for i in range(a):
    for j in range(b):
        if not visit[i][j]:
            visit[i][j]=1
            queue.append([i,j])
            area.append(1)
            while queue:
                y,x = queue.popleft()
                for l in range(4):
                    ny = y+dy[l]
                    nx = x+dx[l]
                    if ny<0 or ny>=a or nx<0 or nx>=b:
                        continue
                    if visit[ny][nx]:
                        continue
                    visit[ny][nx]=1
                    queue.append([ny,nx])
                    area[-1]+=1
print(len(area))
area.sort()
for i in area:
    print(i,end=' ')