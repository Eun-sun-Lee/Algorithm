from collections import deque


def bfs(queue, words, target):
    while queue:
        now, counts = queue.popleft()
        
        if target == now: 
            return counts
        
        for i in range(len(words)):
            cnt = 0
            for a, b in zip(now, words[i]):
                if a != b: cnt += 1
                if cnt > 1: break
            if cnt == 1: 
                queue.append((words[i], counts + 1))
                words[i] = ""
                
        # print(queue)
    return 0
                
    

def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append((begin,0))
    
    answer = bfs(queue, words, target)
    
    return answer