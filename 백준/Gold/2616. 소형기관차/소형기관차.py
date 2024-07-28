import sys 
n = int(sys.stdin.readline())
arr = [0]
l = list(map(int, sys.stdin.readline().split()))
arr += l
limit = int(sys.stdin.readline())

# 누적합 구하기 
prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]
# print(prefix_sum)

def sol(arr, n, prefix_sum, limit):
    dp = [[0] * (n + 1) for _ in range(4)]

    for i in range(1, 4):
        for j in range(n + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i-1][j-limit] + prefix_sum[j] - prefix_sum[j-limit])
    print(dp[3][n])

sol(arr, n, prefix_sum, limit)

