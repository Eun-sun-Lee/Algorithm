import sys 
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
amounts = int(sys.stdin.readline())

def binary_search(n, arr, amounts):
    start = 1 
    end = max(arr)
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        sums = 0
        for i in arr:
            sums += min(i, mid)
        
        if sums <= amounts:
            start = mid + 1
            answer = mid 
        else:
            end = mid - 1
    
    return answer 

print(binary_search(n, arr, amounts))