# a x b = brown + yellow
# a-2 x b-2 = yellow

def solution(brown, yellow):
    answer = []
    
    sum = brown + yellow
    
    a = 3
    b = sum / a
    while a <= b:
        if (a-2) * (b-2) == yellow:
            answer.append(b)
            answer.append(a)
            return answer
            
        a += 1
        b = sum / a
        
        
    return answer