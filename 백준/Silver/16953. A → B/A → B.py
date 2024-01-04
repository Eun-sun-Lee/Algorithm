#BFS
from collections import deque
import math
a,b=map(int,input().split())
queue = deque()
ans=-1

queue.append((a,1))
index=0
while queue:
    q,cnt = queue.popleft()
    if q==b:
        ans=cnt
        break
    if q>b:
        continue
    queue.append((q*2,cnt+1))
    queue.append((int(str(q)+str("1")),cnt+1))

print(ans)