import sys 

N, M = map(int, sys.stdin.readline().split())
# ans = set()
ans = []
ans += list(map(int, sys.stdin.readline().split()))
ans += list(map(int, sys.stdin.readline().split()))

# ans.add(arr1)
# ans.add(arr2)
ans.sort()
print(*ans)