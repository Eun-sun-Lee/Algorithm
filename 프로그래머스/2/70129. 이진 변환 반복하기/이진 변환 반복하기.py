from collections import Counter

def binary_search(val):
    start = 0
    end = 150000
    ret = 0
    
    # 디버깅 2. ret이 2의 제곱승이 되어야함.
#     while start <= end:
#         mid = (start + end) // 2
#         print(mid)
        
#         if val < mid: # 디버깅 1. if val <= mid:
#             end = mid
#         else:
#             start = mid
#             ret = mid
#             break

    num = 2**20
    while True:
        if val >= num:
            ret = num
            break
        num = num // 2
        

    return ret
        

def solution(s):
    answer = [0,0]
    
    while len(s) > 1:
        print(answer)
        cnt = Counter(s)
        answer[0] += 1
        answer[1] += cnt['0']
        cnt_1 = cnt['1']
        num = binary_search(cnt_1)
    
        print(cnt_1, num)
        # 1100 -> 12
        tmp = ""
        while num > 0:
            if cnt_1 > 0:
                tmp += str(cnt_1 // num)
                cnt_1 = cnt_1 % num

            else:
                tmp += "0"
            num = num // 2
        
        s = tmp
        print(tmp)
        
    

        
        # 이진탐색
    # 1100 -> 12
    print(answer)
        
    return answer