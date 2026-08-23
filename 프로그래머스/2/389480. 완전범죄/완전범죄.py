def solution(info, n, m):
    INF = float('inf')
    N = len(info)
    
    # dp[i][j] : i번째 물건(1-indexed)까지 고려했을 때, B의 흔적이 j일 때 A의 최소 흔적
    dp = [[INF] * m for _ in range(N + 1)]
    dp[0][0] = 0 # 0개 고려했을 때: B 흔적 0, A 흔적 0
    
    for i in range(1, N + 1):
        a_trace, b_trace = info[i - 1] # i번째 물건의 흔적 (0-index 기준 info[i-1])
        
        for j in range(m):
            # [선택 1] i번째 물건을 A가 훔치는 경우
            # 이전 단계(i-1)에서 B의 흔적(j)은 그대로이고, A의 흔적만 a_trace 추가됨
            if dp[i - 1][j] != INF:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + a_trace)
            
            # [선택 2] i번째 물건을 B가 훔치는 경우
            # B가 이번에 b_trace를 얻어서 j가 되었으므로, 이전 단계(i-1)에서 B의 흔적은 (j - b_trace)였음
            if j >= b_trace and dp[i - 1][j - b_trace] != INF:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - b_trace])
                
    # N개 물건을 모두 고려한 후 A의 최소 흔적 찾기
    min_a = min(dp[N])
    
    return min_a if min_a < n else -1