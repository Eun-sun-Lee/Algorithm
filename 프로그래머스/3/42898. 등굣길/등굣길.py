def solution(m, n, puddles):
    answer = 0
    not_possible = set()
    memo = [[-1] * m for _ in range(n)]
    dy = [0, 1]
    dx = [1, 0]
    
    
    for i in range(len(puddles)):
        not_possible.add((puddles[i][1] - 1, puddles[i][0] - 1))
        # memo[puddles[i][0] - 1][puddles[i][1] - 1] = -1
        
#     print(memo)
#     print(not_possible)
    
    def dfs(y, x):
        
        if memo[y][x] != -1:
            return memo[y][x]
        
        if y == n-1 and x == m-1:
            return 1
        
        route = 0
        for i in range(2):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m:
                if (ny, nx) not in not_possible:
                    route += dfs(ny, nx)
        memo[y][x] = route % 1000000007
        
        
        return memo[y][x] % 1000000007
        
    answer = dfs(0, 0)
    print(memo)
    return answer