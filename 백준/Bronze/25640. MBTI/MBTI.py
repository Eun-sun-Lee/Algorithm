goal=input()
n=int(input())
num=0
for i in range(n):
    nn=input()
    if goal==nn:
        num+=1
print(num)