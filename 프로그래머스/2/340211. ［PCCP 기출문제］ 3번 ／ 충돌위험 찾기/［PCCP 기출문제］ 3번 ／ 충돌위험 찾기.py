# 문제점 : tarList가 3 이상일 때, 경로
# 시간 초과 
# bfs 돌릴 필요가 없음 (장애물이 있는 것도 아니고, 최단 거리만 찾으면 됨 (r, c) 조건에 따라 )

from collections import deque, Counter
from itertools import zip_longest

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

pairs = []

def solution(points, routes):
    answer = 0

    def bfs(startX, startY, targetX, targetY, path):
    
        while startX != targetX:
            if startX < targetX:
                startX += 1
            else:
                startX -= 1
            path.append((startX, startY))
        
            
        while startY != targetY:
            if startY < targetY:
                startY += 1
            else:
                startY -= 1
            path.append((startX, startY))
        
            
            
                    
        
        return path  # 도달할 수 없는 경우 빈 리스트 반환

    # 각 경로별 BFS 실행
    for r in routes:
        j = deque(r)
        # j = r[:]
        
        path = []
        # print(j[0])
        path = path + [(points[j[0]-1][0]-1, points[j[0]-1][1]-1)]
        
        while len(j) >= 2:
            s = j.popleft()
            # s = j.pop(0)
            n = j[0]
            
            startX = points[s-1][0]-1
            startY = points[s-1][1]-1
            
            # path.append((startX, startY))
            
            targetX = points[n-1][0]-1
            targetY = points[n-1][1]-1

            path = bfs(startX, startY, targetX, targetY, path)
            
            
        # path = path + [(points[j[0]-1][0]-1, points[j[0]-1][1]-1)]
        # print(path)
            
        if path:  # None 또는 빈 리스트([]) 방지
            pairs.append(path)
    

    for pair in zip_longest(*pairs, fillvalue=None):
        filtered_pair = [p for p in pair if p is not None]  # None 값 제거
        cnt = Counter(filtered_pair)

        for k, v in cnt.items():
            if v > 1:
                answer += 1

    return answer
