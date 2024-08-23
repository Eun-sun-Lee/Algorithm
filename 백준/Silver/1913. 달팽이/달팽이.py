import sys 
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

dy = [-1, 0, 1, 0] # 위, 오, 아, 좌
dx = [0, 1, 0, -1] # 위, 오, 아, 좌

graph = [[0] * n for _ in range(n)]
ans = []

def sol():
    cnt = 1
    y = n // 2 
    x = n // 2 
    i = 0
    graph[y][x] = cnt

    while True:
        for j in range(4):
            if j == 0 or j == 2:
                i += 1

            for _ in range(i):
                if cnt == k:
                    ans.append(y + 1)
                    ans.append(x + 1)

                if cnt >= n * n: return

                cnt += 1
                y += dy[j]
                x += dx[j]

                graph[y][x] = cnt 

sol()
for i in graph:
    print(*i)
print(*ans)