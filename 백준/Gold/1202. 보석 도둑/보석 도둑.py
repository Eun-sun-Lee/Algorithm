import sys 
import heapq 

N, K = map(int, sys.stdin.readline().split())
jewel = []
bag = []

for _ in range(N):
    weight, price = map(int, sys.stdin.readline().split())
    heapq.heappush(jewel, (weight, price))

for _ in range(K):
    weight = int(sys.stdin.readline())
    bag.append(weight)
bag.sort()


def sol(jewel, bags):
    result = 0
    candidates = []
    for bag in bags:
        while jewel and jewel[0][0] <= bag:
            w, p = heapq.heappop(jewel)
            heapq.heappush(candidates, -p) 
        if candidates:
            result += -heapq.heappop(candidates)

    print(result)
    
sol(jewel, bag)
