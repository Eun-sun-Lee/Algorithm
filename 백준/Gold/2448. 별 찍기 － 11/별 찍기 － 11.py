import sys
n = int(sys.stdin.readline())

graph = [[' '] * n * 2 for _ in range(n)]

def star(n, r, c):
    if n == 3:
        graph[r][c] = '*'
        for j in range(c - 1, c + 2):
            if j == c: continue
            graph[r + 1][j] = '*'
        for j in range(c - 2, c + 3):
            graph[r + 2][j] = '*'

    else:
        newSize = n // 2
        # center = newSize * 2 - 1
        star(newSize, r, c)
        star(newSize, r + newSize, c - newSize)
        star(newSize, r + newSize, c + newSize) 
star(n, 0, n - 1)
for i in graph:
    print(''.join(i))