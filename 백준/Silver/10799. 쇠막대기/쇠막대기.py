inp = []
stack = []
cnt = 0
ans = 0

inp = list(input())

for i in inp:
    if i == '(':
        stack.append(i)
        cnt = 0
    elif i == ')':
        stack.pop()
        if cnt == 0:
            if len(stack) > 0:
                ans += len(stack) 
        else:
            ans+=1   
        cnt = 1
        

print(ans)