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
    for i in set:
        string=""
        for j in i:
            string+=str(j)
        s.append(int(string))
# print(s)

for i in s:
    if a<=i and i<=b:
        cnt+=1
print(cnt)
    

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