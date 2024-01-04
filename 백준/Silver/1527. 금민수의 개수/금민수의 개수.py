from itertools import product
a,b = map(int,input().split())
cnt = 0
key = []
s = []
for i in range(len(str(a))):
    key.append([4,7])
for i in range(len(str(a)),len(str(b))+1):
    if i!=len(str(a)):
        key.append([4,7])
    set = list(product(*list(key)))
    for i in set:
        string=""
        for j in i:
            string+=str(j)
        s.append(int(string))

for i in s:
    if a<=i and i<=b:
        cnt+=1
print(cnt)