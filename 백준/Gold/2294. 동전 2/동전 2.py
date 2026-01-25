import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
for _ in range(n):
    value = int(sys.stdin.readline())
    coin.append(value)

dp = [10001] * (k + 1)
dp[0] = 0
def coin2(n, coin, k):
    for i in range(n):
        for j in range(1, k + 1):
            if j-coin[i] >= 0:
                dp[j] = min(dp[j], dp[j-coin[i]] + 1)
            else:
                continue
coin2(n, coin, k)

print(dp[k] if dp[k] != 10001 else -1)