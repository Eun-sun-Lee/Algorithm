def solution(triangle):
    answer = 0
    dp = [[0] * (i) for i in range(len(triangle) + 1)]
    dp[0] = [0]
    dp[1] = [triangle[0][0]]

    for i in range(2, len(triangle) + 1):
        for j in range(len(triangle[i - 1])):

            # 왼쪽 위에서 오는 경우
            if j < len(dp[i - 1]):
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + triangle[i - 1][j])

            # 오른쪽 위에서 오는 경우
            if j - 1 >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + triangle[i - 1][j])

    answer = max(dp[-1])
    return answer