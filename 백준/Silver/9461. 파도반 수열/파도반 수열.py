import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())

    def wave(n):
        dp = [0] * n
        dp[0] = dp[1] = dp[2] = 1

        for i in range(3, n):
            dp[i] = dp[i - 2] + dp[i - 3]

        print(dp[n - 1])
    
    if n >= 4:
        wave(n)
    else: print(1)