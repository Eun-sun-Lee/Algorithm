import sys 
n = int(sys.stdin.readline())
graph = [[0] * 3 for _ in range(n + 1)]
dp = [[0] * 3 for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][0], graph[i][1], graph[i][2] = map(int, sys.stdin.readline().split())    
    if i == 1:
        dp[i][0],dp[i][1],dp[i][2] = graph[i][0],graph[i][1],graph[i][2]
# print(graph)
def sol(n, graph):

    for i in range(2, n + 1):
        for j in range(3):
            if dp[i][j - 1] != 0:
                # dp[i][j] = min(dp[i][j - 1],  dp[i - 1][j - 1] + graph[i][j], dp[i - 1][j - 2] + graph[i][j]) # 이 코드의 문제점 -> 이전까지 누적된 dp값이 크면 현재 색상은 아예 안칠해버림. 하지만, 그 다음 입력을 고려할 때 현재 색상을 칠하는 경우가 더 유리한 경우가 있을 수 있음. 따라서, 무조건 색상을 다 칠한 후 마지막행에서 최솟값 비교 
                dp[i][j] = min(dp[i - 1][j - 1] + graph[i][j], dp[i - 1][j - 2] + graph[i][j])
            else:
                dp[i][j] = min(dp[i - 1][j - 1] + graph[i][j], dp[i - 1][j - 2] + graph[i][j])

    print(min(dp[n])) 

sol(n, graph)