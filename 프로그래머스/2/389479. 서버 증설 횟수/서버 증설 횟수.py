import heapq

def solution(players, m, k):
    answer = 0
    
    minServCnt = 0
    server = []

    for i in range(len(players)):
        heapq.heappush(server, (i, 1, players[i])) # 디버깅 2
        # heapq.heappush(server, (i + k, 1, need))

    while server:
        idx, status, cnt = heapq.heappop(server)
        
        
        if status == 1: # 디버깅 2
            if (cnt // m) > minServCnt:
                tmp = (cnt // m - minServCnt) # 디버깅 1
                minServCnt += tmp
                answer += tmp
                heapq.heappush(server, (idx + k, 0, tmp)) # 디버깅 2
        else:
            minServCnt -= cnt
        
        # print(idx, status, cnt, minServCnt, answer)
    
    print(answer)
            
        
    return answer