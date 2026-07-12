def solution(begin, target, words):
    # 타겟 단어가 words 배열에 없으면 애초에 변환 불가능
    if target not in words:
        return 0
    
    # 최솟값을 구하기 위해 정답 변수를 큰 값(또는 단어 배열 길이 + 1)으로 초기화
    answer = len(words) + 1
    visited = [False] * len(words)

    # 두 단어가 한 글자만 다른지 확인하는 함수
    def can_convert(word1, word2):
        diff_count = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                diff_count += 1
            if diff_count > 1:
                return False
        return diff_count == 1

    def dfs(current_word, depth):
        nonlocal answer
        
        # 목표 단어에 도달했다면 현재까지의 변환 횟수(depth)와 비교해 최솟값 갱신
        if current_word == target:
            answer = min(answer, depth)
            return
        
        # 현재 깊이가 이미 구한 최솟값보다 크거나 같다면 더 이상 탐색할 필요 없음 (가지치기)
        if depth >= answer:
            return

        # 사용할 수 있는 모든 단어를 순회
        for i in range(len(words)):
            if not visited[i] and can_convert(current_word, words[i]):
                visited[i] = True  # 방문 처리
                dfs(words[i], depth + 1)  # 재귀 호출
                visited[i] = False # 백트래킹 (다른 경로 탐색을 위해 방문 해제)

    dfs(begin, 0)
    
    # 만약 answer가 초기값 그대로라면 변환할 수 없는 경우이므로 0 반환
    return answer if answer <= len(words) else 0