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

def dfs(i, selectN):
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
    
    # 밑에 두줄 : 원하는 갯수만큼 chickcomb에 값을 채우는 역할
    chickComb.append(i)
    dfs(i + 1, selectN + 1)
    # 밑에 두줄 : distance를 계산한 후 해당 조합을 제거하고, 다른 수를 넣어 새로운 조합을 만드는 역할
    chickComb.pop()
    dfs(i + 1, selectN)

dfs(0,0)
print(ans)