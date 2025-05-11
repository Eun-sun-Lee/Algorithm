def solution(sizes):
    # 항상 긴 쪽을 앞에 오게 정렬
    sizes = [[max(w, h), min(w, h)] for w, h in sizes]
    
    max_w = max(s[0] for s in sizes)  # 긴 쪽 중 최댓값
    max_h = max(s[1] for s in sizes)  # 짧은 쪽 중 최댓값

    return max_w * max_h