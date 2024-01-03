# 계단오르기 (실버3)
import sys
n = int(sys.stdin.readline())
score = []
for _ in range(n):
    i = int(sys.stdin.readline())
    score.append(i)

def ans(score):
    dp = [0] * n
    dp[0] = score[0]
    dp[1] = score[0] + score[1] # 연속해서 두개
    dp[2] = max(score[0] + score[2], score[1] + score[2])
    for i in range(3, n):
        dp[i] = max(dp[i-3] + score[i-1] + score[i], dp[i-2] + score[i])
    # print(dp)
    print(dp[n-1])

if n == 1: print(score[0])
elif n == 2: print(score[1] + score[0])
elif n == 3: print(max((score[0] + score[2]), (score[1] + score[2])))
else: 
    ans(score)


