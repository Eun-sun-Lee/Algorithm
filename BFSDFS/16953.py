#BFS
from collections import deque
import math
a,b=map(int,input().split())
queue = deque()
count=[]
ans=-1

queue.append(a)
index=0
while queue:
    index+=1
    q = queue.popleft()
    if (q&(q-1))==0:
        print(q)
        index=q//2
    if q==b:
        ans=math.ceil(math.sqrt(index))
        break
    q2=q*2
    q1=int(str(q)+str("1"))
    if q2<=b:
        queue.append(q*2)
    if q1<=b:
        queue.append(int(str(q)+str("1")))
print(index)
print(ans)


# # 2 162
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



# # 2 162
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


# 16 81 82 84  [211] 7
# 81 82 84 32 161 [16] 8
# 84 32 161 162 [81]


