import sys 
a, b = map(str, sys.stdin.readline().split())

ans = str(int(a[-1::-1]) + int(b[-1::-1]))
print(int(ans[-1::-1]))
    