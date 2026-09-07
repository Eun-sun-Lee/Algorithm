def solution(k, dungeons):
    global answer, visited
    answer = 0
    visited = [False] * len(dungeons)
    # print(visited)
    
    def dfs(level, curr, cnt):
        global answer, visited
        # if level == len(dungeons):
        #     return 1
        
        answer = max(answer, cnt)
        
        if level == len(dungeons):
            # answer = max(answer, cnt)
            return
        
        for i in range(len(dungeons)):
            if curr >= dungeons[i][0]:
                if curr - dungeons[i][1] >= 0:
                    if visited[i] == False:
                        visited[i] = True
                        dfs(level + 1, curr - dungeons[i][1], cnt + 1)
                        visited[i] = False
        return
    
    dfs(0, k, 0)
    
    print(answer)
                    
        
    return answer