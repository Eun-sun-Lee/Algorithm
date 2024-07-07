# 내가 원하는 r,c가 어느 영역에 있는지 확인하고 그곳만 재귀 돌리기 ..?

import sys 
N, r, c = map(int, sys.stdin.readline().split())

ans = 0

def sol(i, j, n, N):
    global ans

    while n > 1:
        N = N - 1
        n = n // 2
        if i != 0:
            rp = i // n # 몫 
            i = i % n # 나머지
        else:
            rp = 0
            i = 0

        if j != 0:
            cp = j // n # 몫 
            j = j % n # 나머지
        else:
            cp = 0
            j = 0

        th = 2 * rp + cp
        ans += (2 ** N) * (2 ** N) * (th)

sol(r, c, 2 ** N, N)
print(ans)