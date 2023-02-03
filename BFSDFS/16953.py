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

# ex) 2 162
# 2 
# 4 21 [2] 1
# 21 8 41 [4] 2
# 8 41 42 211 [21] 3
# 41 42 211 16 81 [8] 4
# 42 211 16 81 82 411 [41] 5
# 211 16 81 82 411 84 421 [42] 6
# 16 81 82 411 84 421 422 2111 [211] 7
# 81 82 411 84 421 422 2111 32 161 [16] 8
# 411 84 421 422 2111 32 161 162 811 [81]

# # 2 → 4 → 8 → 81 → 162


# ex) 2 162
# 2 
# 4 21 [2] 1
# 21 8 41 [4] 2
# 8 41 42 [21] 3
# 41 42 16 81 [8] 4
# 42 16 81 82 [41] 5
# 16 81 82 84 [42] 6
# 81 82 84 32 161 [16]
# 82 84 32 161 162 [81]
# 84 32 161 162 [82]
# 32 161 162 [84]
# 161 162 [32]
# 162 [161]