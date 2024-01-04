import sys
n = int(sys.stdin.readline())
t = [0] * (n + 1)
p = [0] * (n + 1)
for i in range(1, n + 1):
    a, b = map(int, sys.stdin.readline().split())
    t[i] = a
    p[i] = b

def outCompany(n, t, p):
    dp = [0] * (n + 2) # n + 1일꺼까지 기록
    maxNum = 0 #현재까지의 최대값을 저장할 변수 
    for i in range(1, n + 1):
        maxNum = max(maxNum, dp[i]) # 3) 현재 dp[i]가 최댓값이 아닐 수도 있으므로 이전 최댓값을 불러옴.
        if i + t[i] > n + 1: continue # 1) base case / 종료조건 찾기
        else:
            dp[i + t[i]] = max(maxNum + p[i], dp[i + t[i]]) # 2) 수식 찾기
    print(max(dp))
outCompany(n, t, p)