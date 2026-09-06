import heapq

def solution(players, m, k):
    answer = 0

    minServCnt = 0
    server = []

    for i in range(len(players)):
        heapq.heappush(server, (i, 1, players[i]))   # 수정

    while server:
        idx, status, cnt = heapq.heappop(server)

        if status == 1:   # 수정
            if (cnt // m) > minServCnt:
                tmp = (cnt // m - minServCnt)
                minServCnt += tmp
                answer += tmp
                heapq.heappush(server, (idx + k, 0, tmp))   # 수정
        else:
            minServCnt -= cnt

    return answer