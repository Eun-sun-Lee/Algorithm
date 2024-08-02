import sys 
from collections import deque 

N, M = map(int, sys.stdin.readline().split())

graph = []

marble = deque()
red = [0,0]
blue = [0,0]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for i in range(N):
    l = list(map(str, sys.stdin.readline().strip()))
    graph.append(l)
    for j in range(M):
        if l[j] == "R":
            red[0] = i 
            red[1] = j
        elif l[j] == "B":
            blue[0] = i 
            blue[1] = j

marble.append((red[0], red[1], blue[0], blue[1], 1))


def bfs(N, M, graph, red, blue, marble):
    visited = set()
    visited.add((red[0], red[1], blue[0], blue[1]))

    while marble:
        rr, rc, br, bc, cnt = marble.popleft()
        
        if cnt > 10: return -1

        for i in range(4):
            newRR = rr 
            newRC = rc 
            while True:
                newRR += dy[i]
                newRC += dx[i]

                if graph[newRR][newRC] == "O": 
                    break 
                elif graph[newRR][newRC] == "#":
                    newRR -= dy[i]
                    newRC -= dx[i]
                    break

            newBR = br 
            newBC = bc

            while True:
                newBR += dy[i]
                newBC += dx[i]

                if graph[newBR][newBC] == "O": 
                    break 
                elif graph[newBR][newBC] == "#":
                    newBR -= dy[i]
                    newBC -= dx[i]
                    break
             
            if graph[newBR][newBC] == "O": 
                continue 
            if newRR == newBR and newRC == newBC: 
                if abs(rr - newRR) + abs(rc - newRC) > abs(br - newBR) + abs(bc - newBC):
                    newRR -= dy[i]
                    newRC -= dx[i]
                else:
                    newBR -= dy[i]
                    newBC -= dx[i]

            if graph[newRR][newRC] == "O": return cnt

            if (newRR, newRC, newBR, newBC) not in visited:
                visited.add((newRR, newRC, newBR, newBC))
                marble.append((newRR, newRC, newBR, newBC, cnt + 1))

    return -1

print(bfs(N, M, graph, red, blue, marble))
