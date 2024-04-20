import sys
import math
n = int(sys.stdin.readline())
cnt = 0
arr = [0 for _ in range(10)]
for i in str(n):
    arr[int(i) - 1] += 1
# print(math.ceil(5 / 2))
arr[5] = math.ceil((arr[5] + arr[8]) / 2 ) 
arr[8] = 0
print(max(arr))