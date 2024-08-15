# 3 6 7 8 10 12 14 15 18 20 
# 0 3 1 1 2 2 2 1 3 2 -> 5(2) 10(2) 16(2) 19(1)

# 1 3 6 6 7 9
# 0 2 3 0 1 2 

'''
3
4
2 4 65
0
'''
import sys 
sensor = int(sys.stdin.readline())
home = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

def sol(sensor, home, arr):
    diff = []
    for i in range(1, sensor):
        diff.append(arr[i] - arr[i - 1])
    # print(diff)
    diff.sort()
    # print(diff)
    select = max(sensor - home, 0)
    print(sum(diff[:select]))

if sensor <= 1:
    print(0)
else:
    sol(sensor, home, arr)