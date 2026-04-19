import sys
sys.setrecursionlimit(10**6)

r, c = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(r)]

# -1: 아직 방문 안 함
# 0: 탈출 불가
# 1: 탈출 가능
memo = [[-1] * c for _ in range(r)]
visited = [[False] * c for _ in range(r)]  # 현재 dfs 경로에서 방문 중인지 체크

def dfs(y, x):
    # 격자 밖으로 나가면 탈출 성공
    if not (0 <= y < r and 0 <= x < c):
        return 1

    # 이미 결과를 구한 칸이면 그대로 반환
    if memo[y][x] != -1:
        return memo[y][x]

    # 현재 탐색 경로에서 다시 만났다면 사이클 → 탈출 불가
    if visited[y][x]:
        return 0

    visited[y][x] = True

    if graph[y][x] == 'D':
        ny, nx = y + 1, x
    elif graph[y][x] == 'U':
        ny, nx = y - 1, x
    elif graph[y][x] == 'L':
        ny, nx = y, x - 1
    else:  # 'R'
        ny, nx = y, x + 1

    memo[y][x] = dfs(ny, nx)
    visited[y][x] = False
    return memo[y][x]

answer = 0
for i in range(r):
    for j in range(c):
        answer += dfs(i, j)

print(answer)