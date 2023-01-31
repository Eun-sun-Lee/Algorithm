# 1. 처음
n=int(input())
price=[]
cost=0
for _ in range(n):
    a=int(input())
    price.append(a)
price.sort(reverse=True)

if len(price)<3:
    for i in price:
        cost+=i
else:
    for i in range(len(price)):
        if ((i+1)%3==0):
            continue
        else:
            cost+=price[i]
print(cost)

# 2. 최적화
import sys
input = sys.stdin.readline
n=int(input())

price = [int(input()) for _ in range((n))]
price.sort(reverse=True)
cost = sum(price)

for i in range(2,n,3):
    cost-=price[i]

print(cost)