import sys 
n, m = map(int, sys.stdin.readline().split())
arr = [0]
arr += list(map(int, sys.stdin.readline().split()))

def sol(n, m, arr):
    partSum = [0] * (n + 1)

    for i in range(1, n + 1):
        partSum[i] = partSum[i-1] + arr[i]

    arr.sort() # 변경 

    start = end = 0
    ans = sys.maxsize

    # print(partSum)

    while start <= end and end <= n:
        if (partSum[end] - partSum[start]) < m:
            end += 1
        else: 
            # print(start, end, end - start)
            ans = min(ans, (end - start))
            start += 1 
    if ans == sys.maxsize:
        print(0)
    else:
        print(ans)
sol(n, m, arr)
