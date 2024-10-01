
import sys 
str = sys.stdin.readline().strip()
key = sys.stdin.readline().strip()

def sol(str, key):
    stack = []
    k = len(key)

    for i in range(len(str)):
        stack.append(str[i])

        if ''.join(stack[-k:]) == key:
            for _ in range(k):
                stack.pop()
    
    print(''.join(stack)) if stack else print("FRULA")





sol(str, key)

