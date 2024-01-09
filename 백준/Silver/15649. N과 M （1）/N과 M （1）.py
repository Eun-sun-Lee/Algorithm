# N과 M (1) (실버 3)
import sys
n, m = map(int, sys.stdin.readline().split())
result = [0] * m
arr = [i + 1 for i in range(n)]
checked = [False for _ in range(n)]


def dfs(level):
    if level == m:
        print(*result)
        return

    for i in range(n):
        if checked[i] == True: continue
        result[level] = arr[i]
        checked[i] = True
        dfs(level + 1)
        checked[i] = False
dfs(0)