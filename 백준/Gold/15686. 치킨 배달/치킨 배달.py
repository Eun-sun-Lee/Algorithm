import sys
n, m = map(int,sys.stdin.readline().split())
graph = []
home = []
chicken = []
chickComb = []
ans = sys.maxsize
for i in range(n):
    l = list(map(int,sys.stdin.readline().split()))
    for j in range(n):
        if l[j] == 1: home.append((i+1, j+1))
        elif l[j] == 2: chicken.append((i+1, j+1))
        else: continue
    graph.append(l)

def dfs(selectN, i):
    global ans
    if i > len(chicken): return
    if selectN == m:
        distanceAll = 0
        for r1, c1 in home:
            distance = sys.maxsize
            for j in chickComb:
                r2, c2 = chicken[j]
                distance = min(distance, (abs(r1 - r2) + abs(c1 - c2)))
            distanceAll += distance
        ans = min(ans, distanceAll)
    
    chickComb.append(i)
    dfs(selectN + 1, i + 1)
    chickComb.pop()
    dfs(selectN, i + 1)

dfs(0,0)
print(ans)