def brute_forth(l, ans):
    a = []
    b = []
    c = []
    num1 = [1, 2, 3, 4, 5]
    num2 = [1, 2, 3, 4]
    num3 = [3, 1, 2, 4, 5]
    
    # cnt1 = 0
    # cnt2 = 0
    # cnt3 = 0
    
    cnt = [[0,1], [0,2], [0,3]]
    
# 1번
    for i in range(l // 5 + 1):
        if len(a) == l: break
        for j in range(1, 6):
            a.append(j)
            
            if ans[len(a)-1] == a[len(a)-1]: cnt[0][0] += 1
            if len(a) == l: break
            
# 2번
    for i in range(l // 8 + 1):
        if len(b) == l: break
        for idx, j in enumerate(num2):
            
            b.append(2)
            if ans[len(b)-1] == b[len(b)-1]: cnt[1][0] += 1
            
            if len(b) == l: break
            
            # if i * 8 + idx == l: break
            
            if j == 1:
                b.append(j)
            else:
                b.append(j + 1)
            if ans[len(b)-1] == b[len(b)-1]: cnt[1][0] += 1
            
            if len(b) == l: break
    # 3번
    for i in range(l // 10 + 1):
        if len(c) == l: break
        for j in num3:
            c.append(j)
            if ans[len(c)-1] == c[len(c)-1]: cnt[2][0] += 1
            if len(c) == l: break
            c.append(j)
            if ans[len(c)-1] == c[len(c)-1]: cnt[2][0] += 1
            if len(c) == l: break
                
    
    
    
    print(a)
    print(b)
    print(c)
    # s_cnt = sorted(cnt, key=lambda x:x[1])
    # print(s_cnt)
    cnt.sort(reverse=True)
    print(cnt)
    
    maxNum = max(cnt, key = lambda x:x[0])[0]
    print("!", maxNum)
    ret = []
    
    for i in range(3):
        if maxNum == cnt[i][0]:
            ret.append(cnt[i][1])
    print(ret)
    return sorted(ret)
    
    
        


def solution(answers):
    answer = []
    answerss = answers
    answer = brute_forth(len(answers), answerss)
    
    
    return answer