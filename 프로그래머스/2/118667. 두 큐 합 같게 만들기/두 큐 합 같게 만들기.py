from collections import deque

def solution(queue1, queue2):
    answer = -1
    
    # [수정 1] 전체 합이 홀수면 절대 같게 만들 수 없음
    if (sum(queue1) + sum(queue2)) % 2 != 0:
        return -1
    
    value = (sum(queue1) - sum(queue2)) // 2

    p1 = p2 = -1
    sum_1 = 0
    sum_2 = 0
    
    while True:
        
        if value == 0: 
            answer = 0
            break
        
        if sum_1 - sum_2 == value:
            answer = p1 + p2 + 2
            break
        
        # [수정 2]
        # 기존: if sum_1 <= sum_2:
        if sum_1 - sum_2 < value:
            
            # [수정 3] p1 자체의 범위를 확인
            if p1 + 1 >= len(queue1) + len(queue2):
                break
            
            p1 += 1
            
            if p1 < len(queue1):
                sum_1 += queue1[p1]
            else:
                sum_1 += queue2[p1 - len(queue1)]
                
        else:
            
            # [수정 3] p2 자체의 범위를 확인
            if p2 + 1 >= len(queue1) + len(queue2):
                break
            
            p2 += 1
            
            if p2 < len(queue2):
                sum_2 += queue2[p2]
            else:
                sum_2 += queue1[p2 - len(queue2)]
    
    return answer