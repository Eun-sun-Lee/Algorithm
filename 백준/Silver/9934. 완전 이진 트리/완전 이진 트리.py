import sys 
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(n)]
depth = 0

def recursive(start, end, depth):
    if start >= end : return 

    mid = (start + end) // 2

    recursive(start, mid, depth + 1)
    recursive(mid + 1, end, depth + 1)
    # print(arr[mid], depth)
    graph[depth].append(arr[mid])

recursive(0, 2 ** n - 1, depth)
for i in graph:
    print(*i)