def solution(n, costs):
    answer = []
    graph = []
    ans = 0
    
    for n1, n2, w in costs:
        graph.append((w, n1, n2))
    parent = [0] * (n + 1)
    
    def init():
        for i in range(1, n + 1):
            parent[i] = i
    
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    
    def merge(i, j):
        ii = find(i)
        jj = find(j)
        
        if ii != jj:
            parent[ii] = jj
    
    graph.sort()
    
    init()
    for w, u, v in graph:
        p = find(u)
        q = find(v)
        
        if find(p) != find(q):
            merge(p, q)
            answer.append(w)
    
    ans = sum(answer[:n-1]) # 노드의 갯수 : n-1
    print(answer)
    print(ans)
    
    
            
        
    return ans