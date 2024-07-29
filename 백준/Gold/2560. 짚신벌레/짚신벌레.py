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
    
    # 살아 있는 개체 수 계산
    alive = dp[N]
    if N >= d:
        alive = (alive - dp[N - d]) % 1000
    
    print(alive)

sol(a, b, d, N)
