import sys 
import heapq 

n = int(sys.stdin.readline())
lecture = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    heapq.heappush(lecture, (a, 1)) # start 
    heapq.heappush(lecture, (b, 0)) # end 

cnt = 0
ans = 0
while lecture:
    a, b = heapq.heappop(lecture)
    if b == 1:
        cnt += 1
    else:
        cnt -= 1

    ans = max(cnt, ans)
print(ans)

