a,b=map(int,input().split())
ham = list(input()) # H P
cnt=0

for i in range(len(ham)):
    if ham[i]=="P":
        for j in range(i-b,i+b+1,1):
            if j<0 or j>=a:
                continue
            else:
                if ham[j]=="H":
                    ham[j]="O"
                    cnt+=1
                    break
print(cnt)
        
