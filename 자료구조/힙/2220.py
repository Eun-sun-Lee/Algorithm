import sys
import heapq
n = int(sys.stdin.readline())
ans = []
for i in range(n, 0, -1):
    ans.append(i)
print(*ans)