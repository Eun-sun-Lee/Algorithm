def can_place_routers(distance, houses, C):
    # 첫 번째 집에 공유기를 설치합니다.
    count = 1
    last_position = houses[0]
    
    for i in range(1, len(houses)):
        if houses[i] - last_position >= distance:
            count += 1
            last_position = houses[i]
            if count >= C:
                return True
    return False

def find_max_min_distance(N, C, houses):
    houses.sort()
    
    low = 1
    high = houses[-1] - houses[0]
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        if can_place_routers(mid, houses, C):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return result

# 입력 받기
import sys
N, C = map(int, sys.stdin.readline().split())
houses  = []
for _ in range(N):
    houses.append(int(sys.stdin.readline().strip()))

print(find_max_min_distance(N, C, houses))
