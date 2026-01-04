import sys
n = int(sys.stdin.readline())

graph = [[0] * 3 for _ in range(n)]
dp = [[0] * 3 for _ in range(n + 1)]

for i in range(n):
    graph[i][0], graph[i][1], graph[i][2] = map(int, sys.stdin.readline().split())
dp[0] = graph[0]

for i in range(1, n):
    for j in range(3): # i번째에 j번째 색을 칠했을 때의 최솟값
        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j-2]) + graph[i][j]
print(min(dp[n-1]))
    
