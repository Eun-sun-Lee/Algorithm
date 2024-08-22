import sys 
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())

    def sol(n):
        dp = [1] * (n + 1)

        for i in range(2, n + 1):
            dp[i] += dp[i - 2]
        
        for i in range(3, n + 1):
            dp[i] += dp[i - 3]

        # print(dp)
        print(dp[n])
    
    sol(n)