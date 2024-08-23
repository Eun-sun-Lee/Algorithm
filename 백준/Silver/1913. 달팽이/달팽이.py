import sys 
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

dy = [-1, 0, 1, 0] # 위, 오, 아, 좌
dx = [0, 1, 0, -1] # 위, 오, 아, 좌

graph = [[0] * n for _ in range(n)]

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
                if cnt >= n * n: return

                cnt += 1
                y += dy[j]
                x += dx[j]

                # print(y, x, cnt)
                graph[y][x] = cnt 

sol()
ans = [0, 0]
for i in range(n):
    print(*graph[i])
    for j in range(n):
        if graph[i][j] == k:
            ans[0] = i + 1
            ans[1] = j + 1
print(ans[0], ans[1])
    
