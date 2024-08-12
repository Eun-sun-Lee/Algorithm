import sys
from collections import deque

def bfs(start, target):
    queue = deque()
    queue.append((start, ""))
    visited = set()
    visited.add(start)

    while queue:
        val, dslr = queue.popleft()

        if val == target:
            return dslr

        # D 명령어
        newVal = (2 * val) % 10000
        if newVal not in visited:
            visited.add(newVal)
            queue.append((newVal, dslr + "D"))

        # S 명령어
        newVal = val - 1 if val > 0 else 9999
        if newVal not in visited:
            visited.add(newVal)
            queue.append((newVal, dslr + "S"))

        # L 명령어
        newVal = (val % 1000) * 10 + val // 1000
        if newVal not in visited:
            visited.add(newVal)
            queue.append((newVal, dslr + "L"))

        # R 명령어
        newVal = (val % 10) * 1000 + val // 10
        if newVal not in visited:
            visited.add(newVal)
            queue.append((newVal, dslr + "R"))

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    result = bfs(a, b)
    print(result)
