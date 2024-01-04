import sys
input=sys.stdin.readline

def check(arr): # 연속된 최고 길이의 문자열 확인 함수
    n=len(arr)
    answer=1

    for i in range(n):
        cnt=1
        for j in range(1, n): # 열 검사
            # 같으면 증가, 아니면 초기화
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt=1         
            if cnt > answer:
                answer = cnt
        cnt=1
        for j in range(1, n): # 행 검사
            # 같으면 증가, 아니면 초기화
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt=1
            if cnt > answer:
                answer = cnt
    return answer

n=int(input())
arr=[list(input()) for _ in range(n)]
answer=0

for i in range(n): # 사각형 전체 탐색
    for j in range(n):
        if j+1 < n: # 좌우 바꾸기
            # 자리 바꾸고 검사
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            temp = check(arr)
            if temp > answer: # 최댓값 갱신
                answer = temp
            # 원래대로 복구
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        if i+1 < n: # 상하 바꾸기
            # 자리 바꾸고 검사
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            temp = check(arr)
            if temp > answer: # 최댓값 갱신
                answer = temp
            # 원래대로 복구
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            
print(answer)