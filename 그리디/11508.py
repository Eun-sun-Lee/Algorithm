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



# 0
# 1
# 2
# 3
# 4
# 5
# 6
