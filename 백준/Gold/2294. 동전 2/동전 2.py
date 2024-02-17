import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
for _ in range(n):
    value = int(sys.stdin.readline())
    coin.append(value)

dp = [10001] * (k + 1)
dp[0] = 0
def coin2(n, coin, k):
    for i in range(1, k + 1):
        for j in range(n):
            if i < coin[j] : continue
            dp[i] = min(dp[i], dp[i - coin[j]] + 1)
coin2(n, coin, k)

print(dp[k] if dp[k] != 10001 else -1)