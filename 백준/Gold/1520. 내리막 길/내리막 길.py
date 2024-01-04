# 내리막 길 (골드 3) / DFS-recursion + memorization (성공)
import sys
r, c = map(int, sys.stdin.readline().split())
arr = []
memo = [[-1] * c for _ in range(r)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(r):
    col = list(map(int, sys.stdin.readline().split()))
    arr.append(col)

def dfs(x, y):
    if x == c - 1 and y == r - 1 : return 1

    if memo[y][x] != -1 : return memo[y][x] # 기존에 기록해둔 memo 값이 있을시 사용, 재귀호출 X (memorization 핵심!)

    route = 0
    for i in range(4):
        nextX = x + dx[i]
        nextY = y + dy[i]
        
        if nextX >= 0 and nextX < c and nextY >= 0 and nextY < r:
            if arr[nextY][nextX] < arr[y][x]:
                route += dfs(nextX, nextY)
    memo[y][x] = route
    return memo[y][x]
print(dfs(0,0))