def erastosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return set(str(p) for p in range(2, max_num + 1) if is_prime[p])

def solution(numbers):
    max_num = int(''.join(sorted(numbers, reverse=True)))  # 주어진 숫자들로 만들 수 있는 가장 큰 숫자
    era = erastosthenes(max_num)  # 주어진 숫자로 만들 수 있는 최대 값까지만 소수를 구함
    answer = 0
    checked = [False] * len(numbers)
    current_str = []
    result = set()
    
    def dfs(level):
        if level > 0:
            joined_str = ''.join(current_str)
            if joined_str in era:
                result.add(joined_str)
        
        if level == len(numbers):
            return
        
        for i in range(len(numbers)):
            if not checked[i]:
                checked[i] = True
                current_str.append(numbers[i])
                dfs(level + 1)
                checked[i] = False
                current_str.pop()
    
    dfs(0)
    print(result)
    return len(result)