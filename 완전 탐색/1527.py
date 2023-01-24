# #1. product 풀이
# from itertools import product
# a,b = map(int,input().split())
# cnt = 0
# key = []
# s = []
# for i in range(len(str(a))):
#     key.append([4,7])
# # print(key)
# for i in range(len(str(a)),len(str(b))+1):
#     if i!=len(str(a)):
#         key.append([4,7])
#     set = list(product(*list(key)))
#     print(set)
#     for i in set:
#         string=""
#         for j in i:
#             string+=str(j)
#         s.append(int(string))
# print(s)

# for i in s:
#     if a<=i and i<=b:
#         cnt+=1
# print(cnt)

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

# 10 100
# 4 7
# 7 44 47
# 44 47 74 77
# 47 74 77 444 447
# 74 77 444 447 474 477
# 77 444 447 474 477 744 747
# 444 447 474 477 744 747 774 777
# 447 474 477 744 747 774 777
# 474 477 744 747 774 777
# 477 744 747 774 777
# 744 747 774 777
# 747 774 777
# 774 777
# 777















    

# key = [[4,7],[4,7],[4,7]]
# set = list(product(*list(key)))
# s = []
# for i in set:
#     string=""
#     for j in i:
#         string+=str(j)
#     s.append(int(string))
# print(s)



# 1 10 -> 2
# 11 20 -> 0
# 20 30 -> 0
# 40 50 -> 1
# 1000000 5000000 -> 
# 74 77 -> 

# 4 7 | 1 -> 2
# 44 47 74 77 | 2 -> 2x2
# 444 447 474 477 744 747 774 777 | 3-> 2x2x2

# 1 100 -> 자릿수 계산 1 2 3
# 해당 자릿수마다 key값 만들기 

# 444 
# 444 744 774 777
# 444 474 477
# 444 447 