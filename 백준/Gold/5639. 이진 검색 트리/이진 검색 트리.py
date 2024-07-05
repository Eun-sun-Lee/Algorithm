# 무한입력을 위해 try - except 추가
# 25%에서 시간초과 코드 

import sys
from itertools import zip_longest
sys.setrecursionlimit(10**9)


def postOrder(root):
    if root == None: return 
    else:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data)

def post(start, end):
    if start > end: return 

    mid = end + 1
    for i in range(start + 1, end + 1):
        if arr[start] < arr[i]:
            mid = i
            break 
    post(start + 1, mid - 1)
    post(mid, end)
    print(arr[start])
        

arr = []
while True:
    try:
        n = int(sys.stdin.readline())
        arr.append(n)
    except:
        break
post(0, len(arr) - 1)

