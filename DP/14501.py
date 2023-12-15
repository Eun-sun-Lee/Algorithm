# 퇴사
import sys
n = int(sys.stdin.readline())
t = [0] * (n + 1)
p = [0] * (n + 1)
for i in range(1, n + 1):
    a, b = map(int, sys.stdin.readline().split())
    t[i] = a
    p[i] = b
def ans(n, t, p):
    dp = [0] * (n + 2)
    maxNum = 0
    for i in range(1, n + 1):
        maxNum = max(maxNum, dp[i]) # 위에다 써야 하는 이유 : 퇴사하는 날의 dp값도 업데이트 필요
        if i + t[i] > n + 1: continue
        else:
            dp[i + t[i]] = max(maxNum + p[i], dp[i + t[i]])
    print(max(dp))
ans(n, t, p)