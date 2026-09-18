from collections import deque

def solution(queue1, queue2):
    answer = -1
    
    
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
            # print(sum_1, sum_2, p1, p2)
            break

        if sum_1 - sum_2 < value:
            if p1 + 1 >= len(queue1):
                if p1 + 1 < len(queue1) + len(queue2):
                    p1 += 1
                    sum_1 += queue2[p1 - len(queue1)]
                else: break
            else:
                p1 += 1
                sum_1 += queue1[p1]

        else:
            if p2 + 1>= len(queue2):
                if p2 + 1 < len(queue1) + len(queue2):
                    p2 += 1
                    sum_2 += queue1[p2 - len(queue2)]
                else: break
            else:
                p2 += 1
                sum_2 += queue2[p2]    
    
    return answer