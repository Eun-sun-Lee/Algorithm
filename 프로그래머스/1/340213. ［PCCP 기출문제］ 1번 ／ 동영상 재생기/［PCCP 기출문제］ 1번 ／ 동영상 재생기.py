def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    l = pos.split(":")
    newPos = int(l[0]) * 60 + int(l[1])
    
    s_l = op_start.split(":")
    s_e = op_end.split(":")
    total_l = video_len.split(":")
    
    newStart = int(s_l[0]) * 60 + int(s_l[1])
    newEnd = int(s_e[0]) * 60 + int(s_e[1])
    newTotal = int(total_l[0]) * 60 + int(total_l[1])
    
    if newStart <= newPos <= newEnd:
            newPos = newEnd
    
    for i in commands:
        # if문 순서 주의하기
        if i == "next":
            newPos += 10
        else:
            newPos -= 10
            
        if newPos >= newTotal:
            newPos = newTotal
        elif newPos < 0:
            newPos = 0 
        
        if newStart <= newPos <= newEnd:
            newPos = newEnd
            
    
    if len(str(newPos // 60)) == 1:
        answer += "0"
    answer += str(newPos // 60)
    
    answer += ":"
    
    if len(str(newPos % 60)) == 1:
        answer += "0"
    answer += str(newPos % 60)
        
            
    return answer