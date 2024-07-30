import sys 
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

def sol(n, m, arr):
    remainder = [0] * (m)

    sum = 0
    for i in range(n):
        sum += arr[i]
        remainder[sum % m] += 1

    ans = remainder[0]
    for i in remainder:
        ans += i * (i - 1) // 2
    
    # print(dp)
    print(ans)

sol(n, m, arr)