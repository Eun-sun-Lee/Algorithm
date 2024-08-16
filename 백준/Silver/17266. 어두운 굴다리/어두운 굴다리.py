import sys 
import math 

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
light = list(map(int, sys.stdin.readline().split()))

def binary_search(maxNum):
    left = 0
    right = N
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        
        if maxNum <= mid:
            right = mid - 1
            answer = mid 
        else:
            left = mid + 1
    print(answer)

maxNum = max(light[0] - 0, N - light[len(light) - 1])
for i in range(1, len(light)):
    diff = math.ceil((light[i] - light[i - 1]) / 2)
    maxNum = max(diff, maxNum)

binary_search(maxNum)