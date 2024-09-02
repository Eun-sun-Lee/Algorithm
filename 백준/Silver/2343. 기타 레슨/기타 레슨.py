import sys 
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

def binary_search(n, m, arr):
    left = max(arr)
    right = sum(arr)
    answer = sys.maxsize

    while left <= right:
        mid = (left + right) // 2

        cnt = 1
        sums = 0
        for i in arr:
            sums += i 
            if sums > mid: 
                sums = i
                cnt += 1 
        # print(cnt, mid)
        if cnt > m:
            left = mid + 1
            # answer = mid
            
        else:
            right = mid - 1 
            answer = mid

    return answer 

print(binary_search(n, m, arr))
    