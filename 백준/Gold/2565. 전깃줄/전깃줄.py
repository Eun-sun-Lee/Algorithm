import sys
n = int(sys.stdin.readline())
elec = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    elec.append((start, end))
elec = sorted(elec, key=lambda x:x[0])

def electronic(elec, n):
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if elec[i][1] >= elec[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(n - max(dp))
electronic(elec, n)