import sys 
import heapq

n = int(sys.stdin.readline())
arr = []
dic = {}
alpha = {}
heap = []
ans = 0

for _ in range(n):
    a = sys.stdin.readline().strip()
    arr.append(a)
    for cnt, s in enumerate(a):
        if s not in dic:
            dic[s] = 10 ** (len(a) - cnt - 1)
        else:
            dic[s] += 10 ** (len(a) - cnt - 1)
    

dic = dict(sorted(dic.items(), reverse=True, key=lambda x:x[1]))

num = 9
for k, v in dic.items():
    dic[k] = num 
    num -= 1

for i in arr:
    tmp = 0
    for cnt, j in enumerate(i):
        tmp += dic[j] * (10 ** (len(i) - cnt - 1))
    ans += tmp


print(ans)
