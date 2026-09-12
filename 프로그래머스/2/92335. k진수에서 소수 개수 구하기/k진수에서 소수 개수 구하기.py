def is_prime(num):
    """단일 숫자에 대한 O(sqrt(N)) 소수 판별 함수"""
    if num < 2:
        return False
    # 2부터 num의 제곱근까지만 나누어 떨어지는지 확인
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    
    # 1. k진수 변환
    new_n = ""
    while n > 0:
        new_n += str(n % k)
        n = n // k
    new_n = new_n[::-1]
    
    # 2. '0'으로 split 및 빈 문자열 제거
    arr = list(filter(None, new_n.split('0')))
    
    # 3. 개별 소수 검사 (1,000,000이 넘는 큰 수도 안전하게 판별)
    for i in arr:
        ii = int(i)
        if is_prime(ii):
            answer += 1
            
    return answer