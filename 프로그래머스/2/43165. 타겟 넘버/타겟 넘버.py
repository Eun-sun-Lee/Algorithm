import sys
sys.setrecursionlimit(10 ** 9)

# cnt = 0
oper = [1, -1]

def dfs(valSum, idx, target, numbers):
    global oper
    cnt = 0
    # print(valSum, idx, cnt)
    if idx == len(numbers):
        if valSum == target:
            # print("!!!")
            return 1
        else:
            return 0
    

    for j in range(2):
        num = numbers[idx] * oper[j]
        if idx + 1 <= len(numbers):
            # print(num, valSum + num, idx + 1, cnt)
            cnt += dfs(valSum + num, idx + 1, target, numbers)
    return cnt
            
        
def solution(numbers, target):
    answer = dfs(0, 0, target, numbers)
    
    return answer