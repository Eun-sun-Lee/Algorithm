import sys
n = int(sys.stdin.readline()) #기관차가 끌고 가던 객차의 수
people = [0] + list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline()) #소형기관차가 최대로 끌 수 있는 객차의 수
dp = [[0 for j in range(n+1)] for i in range(4)] #4 = 누적합 1칸 + 소형기관차 3대

for i in range(4):
    for j in range(1, n+1):
        if i == 0: #누적합
            dp[i][j] = dp[i][j-1] + people[j]
        elif j < i*m:
            continue
        elif i == 1 and j >= i*m:
            dp[i][j] = max(dp[i][j-1], dp[0][j]-dp[0][j-m])
        else:
            dp[i][j] = max(dp[i][j-1], (dp[i-1][j-m] + dp[0][j] - dp[0][j-m]))
print(dp[-1][-1])