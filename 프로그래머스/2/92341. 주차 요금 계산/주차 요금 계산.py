import heapq
import math

def solution(fees, records):
    answer = []
    
    # 기본시간(분), 기본요금(원), 단위시간(분), 단위요금(원)
    
    bTime = fees[0]
    bFee = fees[1]
    pTime = fees[2]
    pFee = fees[3]
    
    dic = {}
    
    for str in records:
        arr = str.split(' ')
        time = arr[0].split(':')
        time = int(time[0]) * 60 + int(time[1])
        
        if arr[1] not in dic:
            dic[arr[1]] = [time, 0]
        else:
            if arr[2] == "IN":
                dic[arr[1]][0] = time
            else:
                dic[arr[1]][1] += (time - dic[arr[1]][0])
                dic[arr[1]][0] = -1
    print(dic)
    
    heap = []
    for k, (enter, time) in dic.items():
        if enter != -1:
            time = (60 * 23) + 59
            dic[k][1] += (time - dic[k][0])
            dic[k][0] = -1
            
        if dic[k][1] < bTime:
            heapq.heappush(heap, (k, bFee))
        else:
            tmp = 0
            dic[k][1] -= bTime
            tmp += bFee
            tmp += math.ceil(dic[k][1] / pTime) * pFee
            
            heapq.heappush(heap, (k, tmp))
    print(heap)
    
    while heap:
        car, fee = heapq.heappop(heap)
        answer.append(fee)
            
    return answer