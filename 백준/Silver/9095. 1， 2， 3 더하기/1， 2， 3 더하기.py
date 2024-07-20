import sys 
t = int(sys.stdin.readline())

def dynamic(n):
    dp = [0 for _ in range(n + 1)] 

    dp[0] = 1
    dp[1] = 1 
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[n])


for _ in range(t):
    n = int(sys.stdin.readline())
    if n == 0:
        print(1)
    elif n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        dynamic(n)
