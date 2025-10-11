import sys 
r, c = map(int, sys.stdin.readline().split())
graph = []
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
visited= [[False] * c for _ in range(r)]
ans = 0
alpha = set()

# print(visited)

for _ in range(r):
    l = list(map(str, sys.stdin.readline().strip())) # 문자열 하나하나씩 저장
    alpha.update(l) # ['H', 'M', 'C', 'H', 'H']를 한번에 각각의 요소별로 set에 추가
    graph.append(l)

# used = [graph[0][0]] # (0,0)은 시작좌표이므로 무조건 지남
used = set()
used.add(graph[0][0])

def dfs(level, x, y):
    global used, ans
    
    ans = max(ans, level)

    if level == len(alpha):
        return
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < r and 0 <= nx < c:
            if visited[ny][nx] == False:
                # if graph[ny][nx] not in used:
                #     visited[ny][nx] = True
                #     used.append(graph[ny][nx])
                #     dfs(level + 1, nx, ny)
                #     used.pop()
                #     visited[ny][nx] = False
                if graph[ny][nx] not in used:
                    visited[ny][nx] = True
                    used.add(graph[ny][nx])
                    dfs(level + 1, nx, ny)
                    used.remove(graph[ny][nx])
                    visited[ny][nx] = False

dfs(1, 0, 0)
print(ans)



