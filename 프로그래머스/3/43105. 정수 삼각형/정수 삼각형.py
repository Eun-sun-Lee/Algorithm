def solution(triangle):
    memo = [[-1] * (i + 1) for i in range(len(triangle))]
    
    # 1. sum_x 인자를 제거하여 (y, x) 위치 이후의 최대합만 구하도록 변경
    def dfs(y, x):
        # 이미 계산된 값이 있으면 바로 반환
        if memo[y][x] != -1:
            return memo[y][x]
        
        # 기저 조건: 바닥(바탕) 행에 도착하면 해당 위치의 값을 반환
        if y == len(triangle) - 1:
            memo[y][x] = triangle[y][x]
            return memo[y][x]
        
        # 2. 하위 경로(왼쪽 아래, 오른쪽 아래) 탐색
        left = dfs(y + 1, x)
        right = dfs(y + 1, x + 1)
        
        # 3. 현재 위치의 값 + 아래 경로 중 더 큰 값 저장
        memo[y][x] = triangle[y][x] + max(left, right)

        return memo[y][x]
        
    return dfs(0, 0)