import sys
import math

def cycle(n, l):
    board = [0] * (n + 1)
    num = 0
    for i in range(1, n + 1):
        j = i
        while j <= n:
            if board[j] == 1: break
            if i == j: num += 1
            board[j] = 1
            j = l[j]
    return num

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    # l = list(map(int, sys.stdin.readline().split()))
    l = list(map(int, input().split()))
    l.insert(0, 0)
    print(cycle(n, l))