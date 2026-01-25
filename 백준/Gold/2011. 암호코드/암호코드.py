import sys 
sys.setrecursionlimit(10 ** 9)

str = list(map(int, sys.stdin.readline().strip()))
dp = [0] * (len(str) + 1)
leng = len(str)

dp[0] = 1
dp[1] = 1

if str[0] == 0:
	print(0)
else:
	for i in range(2, len(str) + 1):
		for j in range(2):
			if j == 0: # 25114 01234  
				if str[i-1] > 0:
					dp[i] += dp[i-1]
			else:
				if 10 <= str[i-2] * 10 + str[i-1] <= 26:
					dp[i] += dp[i-2]
	print(dp[leng] % 1000000)