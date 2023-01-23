from collections import deque

a,b = map(int,input().split())
visit = [[0]*b for _ in range(a)]
for i in range(a):
    c = input()
    for j in range(b):
        visit[i][j] = int(c[j])
#BFS
queue = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(a):
    for j in range(b):
        if visit[i][j]==1:
            queue.append([i,j])
            visit[i][j]+=1
            while queue:
                y,x = queue.popleft()
                for l in range(4):
                    ny=dy[l]+y
                    nx=dx[l]+x
                    if nx>=b or nx<0 or ny>=a or ny<0:
                        continue
                    if visit[ny][nx]!=1:
                        continue
                    visit[ny][nx]=visit[y][x]+1
                    queue.append([ny,nx])
print(visit[a-1][b-1]-1)
                    
