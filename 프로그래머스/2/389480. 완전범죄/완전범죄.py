def solution(info, n, m):
    INF = float('inf')
    
    # dp[j] : B의 누적 흔적이 정확히 'j'일 때, A가 남긴 '최소 누적 흔적'
    dp = [INF] * m
    dp[0] = 0  # 초기 상태: B의 흔적 0일 때, A의 흔적도 0

    for a_trace, b_trace in info:
        # 1차원 DP 중복 계산을 방지하기 위해 B의 흔적(j)을 역순(m-1 -> 0)으로 탐색
        for j in range(m - 1, -1, -1):
            if dp[j] == INF:
                continue
            
            # [선택 2] B가 물건을 가져가는 경우 (B의 흔적이 m 미만일 때만)
            # 이전 상태 dp[j]에 B의 흔적 b_trace를 더해 j + b_trace 칸을 갱신
            if j + b_trace < m:
                dp[j + b_trace] = min(dp[j + b_trace], dp[j])
            
            # [선택 1] A가 물건을 가져가는 경우
            # B의 흔적 j는 그대로 유지되고, A의 흔적만 a_trace 추가됨
            dp[j] = dp[j] + a_trace

    # 모든 물건을 고려한 후 A의 최소 흔적 찾기
    min_a = min(dp)
    
    # A의 흔적이 n 미만이면 정답, n 이상이면 붙잡히므로 -1 반환
    return min_a if min_a < n else -1