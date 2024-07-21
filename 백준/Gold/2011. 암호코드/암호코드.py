import sys 
sys.setrecursionlimit(10 ** 9)

str = sys.stdin.readline()
memo = [[-1] * 2 for _ in range(len(str))]

def dfs(idx, str, ii):
    if idx == len(str) - 1:
        return 1 

    if memo[idx][ii] != -1: return memo[idx][ii]

    way = 0
    for i in range(1, 3):
        nIdx = idx + i
        if nIdx < len(str) and 0 < int(str[idx:nIdx]) <= 26 and str[idx:nIdx][0] != "0": # 2. 0처리 추가 (0 < )
            way += dfs(nIdx, str, i - 1)
        memo[idx][ii] = way % 1000000
    return memo[idx][ii] % 1000000

print(dfs(0, str, 0) % 1000000)
# print(int("01")) -> 1