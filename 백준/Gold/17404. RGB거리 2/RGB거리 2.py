import sys 
n = int(sys.stdin.readline())
graph = [[0] * 3 for _ in range(n + 1)]
dp = [[0] * 3 for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][0], graph[i][1], graph[i][2] = map(int, sys.stdin.readline().split())    
def sol(n, graph):
    ans = sys.maxsize
    for t in range(3):
        dp[1][0],dp[1][1],dp[1][2] = 10000,10000,10000
        dp[1][t] = graph[1][t]
        # print(dp)

        for i in range(2, n + 1):
            for j in range(3):
                dp[i][j] = min(dp[i - 1][j - 1] + graph[i][j], dp[i - 1][j - 2] + graph[i][j])
        dp[n][t] = sys.maxsize
        ans = min(ans, min(dp[n]))
    print(ans)
sol(n, graph)