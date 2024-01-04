from re import L
import sys
n = int(sys.stdin.readline())
dp = [0] * 1001
dp[1] = 1 # SK
dp[2] = 2 # CY
dp[3] = 1 
for i in range(4, n + 1):
    if dp[i - 1] == 1 or dp[i - 3] == 1:
        dp[i] = 2
    else:
        dp[i] = 1
print('CY' if dp[n] == 1 else 'SK')