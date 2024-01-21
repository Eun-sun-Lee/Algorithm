import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def bitonic(n, arr):
    dp = [1] * n
    dp2 = [1] * n

    maxNum = 0
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                maxNum = max(dp[i], maxNum)
    
    for i in range(n - 2, -1, -1):
        for j in range(i, n):
             if arr[i] > arr[j]:
                 dp2[i] = max(dp2[i], dp2[j] + 1)


    ans = []
    for i in range(n):
        ans.append((dp[i] + dp2[i]))
    print(max(ans) - 1)

bitonic(n, arr)
