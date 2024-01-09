# N과 M (3) (실버 3)
import sys
n, m = map(int, sys.stdin.readline().split())
result = [0] * m
arr = [i + 1 for i in range(n)]

def dfs(level):
    if level == m:
        print(*result)
        return

    for i in range(n):
        result[level] = arr[i]
        dfs(level + 1)
dfs(0)