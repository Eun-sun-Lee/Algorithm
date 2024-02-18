import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    c = list(map(int, sys.stdin.readline().split()))
    price = int(sys.stdin.readline())
    dp = [[0] * (price + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dp[i][0] = 1

    def coin(n, c, price):
        for i in range(1, n + 1):
            coinComb = 0
            j = 0
            for j in range(1, price + 1):
                if j - c[i - 1] < 0 : coinComb = 0
                else: coinComb = dp[i][j - c[i - 1]]
                dp[i][j] = dp[i - 1][j] + coinComb
                
    coin(n, c, price)
    print(dp[n][price])