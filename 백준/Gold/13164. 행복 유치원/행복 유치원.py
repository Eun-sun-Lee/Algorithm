import sys 
n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

def sol(n, s, arr):
    minusArr = []

    for i in range(1, n):
        minusArr.append((arr[i] - arr[i - 1]))
    # print(minusArr)
    minusArr.sort()
    print(sum(minusArr[:n - s]))

sol(n, s, arr)