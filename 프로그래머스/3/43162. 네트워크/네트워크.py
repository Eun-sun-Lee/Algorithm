import heapq

def solution(n, computers):
    answer = 0
    
    graph = [[] for _ in range(len(computers) + 1)]
    
    # graph 만들기
    for i in range(len(computers)):
        for j in range(len(computers)):
            if i == j: continue
            
            if computers[i][j] == 1:
                graph[i + 1].append(j + 1)
    print(graph)
    
    # MST - prim
    Q = []
    visited = [False for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        if visited[i] == True: continue
        
        heapq.heappush(Q, i)

        while Q:
            v = heapq.heappop(Q)

            for nv in graph[v]:
                if visited[nv] == False:
                    visited[nv] = True 
                    heapq.heappush(Q, nv)
        answer += 1
        
        
        
    
    
    return answer