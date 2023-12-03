import sys

def find(x):
    while pt[x] != x:
        pt[x] = pt[pt[x]]
        x = pt[x]
    return x

def in_the_same_set(p, q):
    return find(p) == find(q)

def union(p, q):
    i = find(p)
    j = find(q)
    if i != j:
        pt[i] = j

n, m = map(int, sys.stdin.readline().split())
pt = [i for i in range (0, n + 1)]
# print(pt)
for _ in range(m):
    a, v1, v2 = map(int, sys.stdin.readline().split())
    if a == 0:
        union(v1, v2)
    else:
        if in_the_same_set(v1, v2) == True:
            print("YES")
        else:
            print("NO")
