import sys 
n, k = map(int, sys.stdin.readline().split())
coin = [0] 

for _ in range(n):
    num = int(sys.stdin.readline())
    coin.append(num)

def sol(n, k, coin):
    dp = [0] * (k + 1)

    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if j - coin[i] >= 0: 
                # dp[i] = dp[i - 1] + dp[j - coin[i]]
                dp[j] += dp[j - coin[i]] 
    # print(dp)
    print(dp[k])
sol(n, k, coin)