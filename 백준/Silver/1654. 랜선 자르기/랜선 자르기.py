# 유사 그리디 
import sys 
K, N = map(int, sys.stdin.readline().split())
lans = []
for _ in range(K):
    lan = int(sys.stdin.readline())
    lans.append(lan)

def binary_search(K, N, lans):
    start = 1
    end = max(lans)
    answer = 0

    while start <= end: # 0 1
        mid = (start + end) // 2

        cnt = 0
        for lan in lans:
            cnt += (lan // mid ) # ZeroDivisionError

        if cnt >= N:
            start = mid + 1 
            answer = mid 
        else:
            end = mid - 1
    return answer 

print(binary_search(K, N, lans))

