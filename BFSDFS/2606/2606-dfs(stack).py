v = int(input())
e = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    stack = [x]
    visited[x] = True
    count = 0
    while stack:
        node = stack.pop()
        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                stack.append(next)
                count += 1
    return count

visited = [False for _ in range(v+1)]
print(dfs(1))