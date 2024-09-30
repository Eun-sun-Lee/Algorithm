from collections import deque 

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def solution(maps):
    answer = 0
    
    n = len(maps) - 1
    m = len(maps[0]) - 1
    
    queue = deque()    
    queue.append((1, 0,0))
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    while queue:
        cnt, y, x = queue.popleft()
        
        if y == n and x == m:
            if maps[y][x] == 0:
                cnt = -1
                
            return cnt
        
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            
            if 0 <= ny <= n and 0 <= nx <= m:
                if visited[ny][nx] == False and maps[ny][nx] == 1:
                    visited[ny][nx] = True 
                    queue.append((cnt + 1, ny, nx))
                

    
    return -1