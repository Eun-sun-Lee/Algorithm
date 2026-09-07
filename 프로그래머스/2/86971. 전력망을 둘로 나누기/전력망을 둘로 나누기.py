import copy

def solution(n, wires):
    global graph, tmp, counts
    answer = float('inf')
    
    graph = [[] for _ in range(n + 1)]
    
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    
    
    def dfs(idx, cnt):
        global graph, tmp, counts

        # counts = max(counts, cnt) # 디버깅 2
        
        for i in tmp[idx]:
            if visited[i] == False:
                visited[i] = True 
                dfs(i, cnt + 1)
                # visited[i] = False # 디버깅 3 한번만 가면 끝임
                counts += 1 #디버깅 2
                
    
    for a,b in wires:
        # visited = [[False] for _ in range(n + 1)] # 디버깅 1
        visited = [False for _ in range(n + 1)] # 디버깅 1
        tmp = copy.deepcopy(graph) # 포인트 1 graph.copy()랑 혼돈 주의 (얕은 복사)

        tmp[a].remove(b)
        tmp[b].remove(a)
        
        
        counts = 0
        visited[a] = True # 디버깅 4 시작 노드 방문 처리 누락
        dfs(a, 0)
        count1 = counts
        
        counts = 0
        visited[b] = True
        dfs(b, 0)
        count2 = counts
        
        answer = min(abs(count1-count2), answer)

    
    # print(graph)
    

    return answer

