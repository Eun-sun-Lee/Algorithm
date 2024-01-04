# 피보나치 수4 (실버5) 
import sys
n = int(sys.stdin.readline())
dp = (n + 1) * [0]
dp[0] = 0
if n != 0:
    dp[1] = 1

for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
print(dp[n] % 1000000007)