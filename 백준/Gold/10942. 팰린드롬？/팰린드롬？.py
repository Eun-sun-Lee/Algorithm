import sys
sys.setrecursionlimit(10**9)

# 7
'''
1 -> [[1][-1][-1][-1][-1][-1][-1]] 1,2,3,4,5,6,7
2 -> [[1][-1][-1][-1][-1][-1]] 2,3,4,5,6,7
3 -> [[1][-1][-1][-1][-1]] 3,4,5,6,7
4 -> [[1][-1][-1][-1]] 4,5,6,7
5 -> [[1][-1][-1]]  5,6,7
6 -> [[1][-1]] 6,7 
7 -> [[1]] 7,7
'''

def palindrome(S, E):
    global n, m, memo, arr
    if S >= E or S < 0 or E < 0: return 1

    if memo[S][E - S] != -1:
        # print("1", memo[S][E-S], S, E-S)
        return memo[S][E - S]
    elif arr[S] == arr[E]:
        # print("2", memo[S][E-S], S, E-S)
        memo[S][E - S] = palindrome(S + 1, E - 1)
        # print("2-2", memo[S][E-S], S, E-S)
        return memo[S][E - S]
    else:
        # print("3", memo[S][E-S], S, E-S)
        memo[S][E - S] = 0
        return 0


n = int(sys.stdin.readline())
memo = [[-1] * (n - i) for i in range(n)]

arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    memo[a - 1][b - a] = palindrome(a - 1, b - 1)
    print(memo[a - 1][b - a])
    # print(memo)