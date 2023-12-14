# # 최적화 전
# import sys
# n = int(sys.stdin.readline())

# def tile(n):
#     dp = [0] * (n + 1)
#     dp[1] = 1
#     if n > 1: # n = 1일 때 예외처리 추가
#         dp[2] = 3
#     if n >= 3:
#         for i in range(3, n + 1):
#             if i % 2 == 0:
#                 dp[i] = 3 + ((dp[i - 1] - 1) * 2)
#             else:
#                 dp[i] = (dp[i - 1] - 1) * 2 + 1
#     print(dp[n] % 10007)
#     return        

# tile(n)

# 최적화 후
import sys
n = int(sys.stdin.readline())

def tile(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    if n > 1: # n = 1일 때 예외처리 추가
        dp[2] = 3
    if n >= 3:
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + (dp[i - 2] * 2)) % 10007 # 2 x n 타일을 만드려면 바로 n -1에서 하나 추가하는 방법과 n -2에서 두개 추가하는법
    print(dp[n] % 10007)
    return        

tile(n)


