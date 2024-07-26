import sys 
n, limit = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
maxNum = 0
arr = [0, 0, 0]
checked = [False] * n

def dfs(start, level):
    global maxNum, l, n, limit
    if level >= 3:
        if sum(arr) <= limit:
            maxNum = max(sum(arr), maxNum)
        return

    for i in range(start, n):
        if checked[i] == True : continue 
        # print(level, i)
        arr[level] = l[i] 
        checked[i] = True 
        dfs(i + 1, level + 1)
        checked[i] = False 
    
dfs(0, 0)
print(maxNum)
    