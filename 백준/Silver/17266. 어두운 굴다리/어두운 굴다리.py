import sys 
import math 

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
light = list(map(int, sys.stdin.readline().split()))


maxNum = max(light[0] - 0, N - light[len(light) - 1])
for i in range(1, len(light)):
    diff = math.ceil((light[i] - light[i - 1]) / 2)
    maxNum = max(diff, maxNum)

print(maxNum)
