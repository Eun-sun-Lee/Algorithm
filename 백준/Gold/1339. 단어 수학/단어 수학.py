def backtracking(index, word, alphabet_list, value, visited, n):
    global max_sum
    if index == len(alphabet_list):
        # 모든 알파벳에 숫자가 할당된 경우, 합을 계산
        total_sum = 0
        for w in word:
            num = 0
            for char in w:
                num = num * 10 + value[alphabet_list.index(char)]
            total_sum += num
        max_sum = max(max_sum, total_sum)
        return
    
    # 가능한 숫자들 (0~9) 중에서 할당해보는 백트래킹
    for i in range(10):
        if not visited[i]:
            visited[i] = True
            value[index] = i
            backtracking(index + 1, word, alphabet_list, value, visited, n)
            visited[i] = False
            value[index] = 0

def main():
    global max_sum
    n = int(input())  # 단어의 개수
    word = [input().strip() for _ in range(n)]  # 단어들 입력 받기
    
    alphabet_list = []
    for w in word:
        for char in w:
            if char not in alphabet_list:
                alphabet_list.append(char)  # 알파벳이 alphabet_list에 없으면 추가
    
    visited = [False] * 10  # 숫자 0~9 사용 여부
    value = [0] * len(alphabet_list)  # 각 알파벳에 대응하는 숫자 저장
    max_sum = -float('inf')  # 최대값 초기화
    
    backtracking(0, word, alphabet_list, value, visited, n)
    
    print(max_sum)

if __name__ == "__main__":
    main()
