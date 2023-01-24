# #1. product 풀이
from itertools import product
a,b = map(int,input().split())
cnt = 0
key = []
s = []
for i in range(len(str(a))):
    key.append([4,7])
# print(key)
for i in range(len(str(a)),len(str(b))+1):
    if i!=len(str(a)):
        key.append([4,7])
    set = list(product(*list(key)))
    print(set)
    for i in set:
        string=""
        for j in i:
            string+=str(j)
        s.append(int(string))
print(s)

for i in s:
    if a<=i and i<=b:
        cnt+=1
print(cnt)

#2. bfs 풀이
from collections import deque

a,b = map(int,input().split())
cnt=0
queue= deque()
queue.append(4)
queue.append(7)

while queue:
    q = queue.popleft()
    if q<=b:
        if a<=q: 
            cnt+=1
        queue.append(q*10+4)
        queue.append(q*10+7)
print(cnt)
