import sys 

n, m = map(int, sys.stdin.readline().split())
memoryArr = list(map(int,sys.stdin.readline().split()))
cost = list(map(int,sys.stdin.readline().split()))


def bag(n, m, memory, cost):
    dp = [[0] * (sum(cost) + 2) for _ in range(n + 1)]
    minCost = sys.maxsize

    for i in range(1, n + 1):
        for j in range(sum(cost) + 1):
            if j - cost[i - 1] < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i - 1]] + memory[i - 1])
        
            if dp[i][j] >= m:
                minCost = min(minCost, j)

            
        # print(dp)
    print(minCost)

bag(n, m, memoryArr, cost)
