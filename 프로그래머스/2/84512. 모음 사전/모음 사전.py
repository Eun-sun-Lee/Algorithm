def dfs(level):
    global dict, result, cnt
    cnt += 1
    
    if ''.join(result) not in dict:
        dict[''.join(result)] = cnt
    
    if level == 5:
        return
    
    for i in range(5):
        result[level] = alpha[i]
        dfs(level + 1)
        result[level] = ""
    
    
    

def solution(word):
    global dict, alpha, result, cnt
    alpha = ['A', 'E', 'I', 'O', 'U']
    result = ["" for _ in range(5)]
    dict = {}
    cnt = -1
    
    dfs(0)
    
    answer = -1
    if word in dict:
        answer = dict[word]

    return answer