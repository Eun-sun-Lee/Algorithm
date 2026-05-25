import sys
sys.setrecursionlimit(10 ** 9)

oper = [1, -1]

def dfs(valSum, idx, target, numbers):
    global oper
    
    if idx == len(numbers):
        if valSum == target:
            return 1
        else:
            return 0
        
    cnt = 0
    for j in range(2):
        num = numbers[idx] * oper[j]
        if idx + 1 <= len(numbers): # list out of index 방지
            cnt += dfs(valSum + num, idx + 1, target, numbers)
    return cnt
        
def solution(numbers, target):
    answer = dfs(0, 0, target, numbers)
    return answer