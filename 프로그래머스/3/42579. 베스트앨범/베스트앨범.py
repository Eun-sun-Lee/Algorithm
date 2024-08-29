
def solution(genres, plays):
    dict = {}
    sumDict = {}
    answer = []
    n = len(genres)
    
    for i in range(n):
        if genres[i] not in dict:
            dict[genres[i]] = [(plays[i], -i)]
            sumDict[genres[i]] = plays[i]
        else:
            dict[genres[i]].append((plays[i], -i))
            sumDict[genres[i]] += plays[i]
            
    sumDict = sorted(sumDict.items(), key = lambda x:x[1], reverse = True)
    
    print(sumDict)
    
    for i in range(len(sumDict)):
        dict[sumDict[i][0]].sort(reverse = True)
        print(dict[sumDict[i][0]])
        
        # print(sumDict[i][0])
        # answer += dict[sumDict[i][0]][:2]
        cnt = 0
        for j in range(len(dict[sumDict[i][0]])):
            answer.append(-dict[sumDict[i][0]][j][1])
            cnt += 1
            if cnt >= 2: break
        
    
    # print(sumDict)
    
    return answer