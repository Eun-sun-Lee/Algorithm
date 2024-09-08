def erastosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return set(str(p) for p in range(2, max_num + 1) if is_prime[p])


def dfs(level, numbers):
    global visited, str, result, era_list
    
    s = ''.join(str)
    print(s)
    
    if s not in result and s in era_list:
        result.append(s)
        # str[level] = ''
    
    if level == len(numbers):
        return
        
        
    for i in range(len(numbers)):
        if visited[i] == False:
            visited[i] = True 
            str[level] = numbers[i]
            dfs(level + 1, numbers)
            visited[i] = False
            str[level] = ''
            
    
def solution(numbers):
    global visited, str, result, era_list
    
    max_num = int(''.join(sorted(numbers, reverse=True)))  # 주어진 숫자들로 만들 수 있는 가장 큰 숫자
    era_list = erastosthenes(max_num)
    visited = [False] * len(numbers)
    str = ['' for _ in range(len(numbers))]
    result = []
    
    dfs(0, numbers)
    
    return len(result)