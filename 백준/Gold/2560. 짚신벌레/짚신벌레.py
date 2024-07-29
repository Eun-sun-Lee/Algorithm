import sys 
a, b, d, N = map(int, sys.stdin.readline().split())

def sol(a, b, d, N):
    dp = [0] * (N + 1)

    # 초기화
    for i in range(a):
        dp[i] = 1
    
    # a ~ b 번식
    for i in range(a, N + 1):
        dp[i] = (dp[i - 1] + dp[i - a]) % 1000

        if i >= b:
            dp[i] = (dp[i] - dp[i - b]) % 1000
    # print(dp)
    
    if N >= d: # 에외 처리
        print((dp[N] - dp[N - d]) % 1000)
    else:
        print(dp[N] % 1000)
        
sol(a, b, d, N)