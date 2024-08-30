# 주어진 항공권은 모두 사용해야 합니다.
def dfs(a, cnt, travel):
    global answer 
    if cnt == n:
        answer = [travel[i:i+3] for i in range(0, len(travel), 3)]
        print(answer)
        return answer
    
    if a in dict:
        for i in range(len(dict[a])):  
            # print(dict[a][i])
            t = dict[a][i]
            if t[1] == 0:
                t[1] = 1
                result = dfs(t[0], cnt + 1, travel + t[0])
                if result:
                    return result 
                else: 
                    t[1] = 0


def solution(tickets):
    global dict, visitedSet, answer, n
    n = len(tickets) + 1
    travel = "ICN"
    answer = ["ICN"]
    dict = {}
    
    for s, e in tickets:
        if s not in dict:
            dict[s] = [[e, 0]]
        else:
            dict[s].append([e, 0])

    for t in dict:
        dict[t].sort()
        
    dfs("ICN", 1, travel)
    print(dict)
    print(dict["ICN"][0])
            
    return answer