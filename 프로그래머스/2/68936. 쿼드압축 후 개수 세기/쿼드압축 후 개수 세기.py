def solution(arr):
    # answer[0]은 0의 개수, answer[1]은 1의 개수
    answer = [0, 0]
    
    def solve(size, r, c):
        # 1. 현재 영역이 모두 같은 숫자인지 체크
        first_val = arr[r][c]
        is_same = True
        
        for i in range(r, r + size):
            for j in range(c, c + size):
                if arr[i][j] != first_val:
                    is_same = False
                    break
            if not is_same:
                break
        
        # 2. 모두 같은 숫자라면 압축 가능! 해당 숫자 카운트를 1 증가시키고 종료
        if is_same:
            answer[first_val] += 1
            return
        
        # 3. 다른 숫자가 섞여 있다면 4분할하여 재귀 호출
        half = size // 2
        solve(half, r, c)                  # 왼쪽 위
        solve(half, r, c + half)           # 오른쪽 위
        solve(half, r + half, c)           # 왼쪽 아래
        solve(half, r + half, c + half)    # 오른쪽 아래

    # 전체 배열 크기부터 시작
    solve(len(arr), 0, 0)
    
    return answer