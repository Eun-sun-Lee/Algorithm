import sys
from collections import deque

cnt=0
n = 4*(int(sys.stdin.readline()))-3
queue = deque()
print(n*'*')
for i in range(n-2,-1,-2):
    if cnt%2==0:
        queue.append("*")
    else:
        queue.append(" ")
    for j in queue:
        print(j,end='')
    if cnt%2==0:
        print(i*" ",end='')
    else:
        print(i*"*",end='')
    for j in range(len(queue)-1,-1,-1):
        print(queue[j],end='')
    print()
    cnt+=1
if n!=1:
    cnt=0
    for i in range(3,n,2):
        queue.pop()
        for j in queue:
            print(j,end='')
        if cnt%2==0:
            print(i*" ",end='')
        else:
            print(i*"*",end='')
        for j in range(len(queue)-1,-1,-1):
            print(queue[j],end='')
        print()
        cnt+=1
    print(n*'*')









