# 스티커 (실버 1)
import sys
t = int(sys.stdin.readline())

def sticker(arr, b):
    for i in range(1, b):
        for j in range(2):
            if j == 0: dp[j][i] = max(dp[1][i-1], dp[0][i-1]-arr[0][i-1]) + arr[j][i] 
            else: dp[j][i] = max(dp[0][i-1], dp[1][i-1]-arr[1][i-1]) + arr[j][i]

while(t > 0):
    t-=1
    b = int(sys.stdin.readline())
    arr = []
    dp = [b * [0] for _ in range(2)]
    for _ in range(2):
        l = list(map(int, sys.stdin.readline().split()))
        arr.append(l)
    # print(arr)
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    sticker(arr, b)
    print(max(dp[1][b-1], dp[0][b-1]))
    # print(dp) 