# N과 M (4) (실버 3)
import sys
n, m = map(int, sys.stdin.readline().split())
result = [0] * m
arr = [i + 1 for i in range(n)]
checked = [False for _ in range(n)]

def dfs(level, begin):
    if level == m:
        print(*result)
        return

    for i in range(begin, n):
        result[level] = arr[i]
        dfs(level + 1, i)
dfs(0, 0)