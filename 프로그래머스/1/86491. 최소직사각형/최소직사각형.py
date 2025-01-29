def solution(sizes):
    answer = 0
    
    w_max = max(sizes, key = lambda x: x[0])[0]
    h_max = max(sizes, key = lambda x: x[1])[1]

    if max(w_max, h_max) == w_max: 
        # n_h_max = h_max
        for i in range(len(sizes)):
            # if sizes[i][0] < sizes[i][1] and n_h_max > sizes[i][0]:
            if sizes[i][0] < sizes[i][1]:
                sizes[i][1] = sizes[i][0]
        h_max = max(sizes, key = lambda x: x[1])[1]
    else:
        for i in range(len(sizes)):
            if sizes[i][0] > sizes[i][1]:
                sizes[i][0] = sizes[i][1]
        w_max = max(sizes, key = lambda x: x[0])[0]
        
    answer = w_max * h_max
                
            
    
    
    
        
        
    return answer