def solution(n, bans):
    # 1. 봉인된 주문을 숫자로 변환
    def to_num(s):
        num = 0
        for c in s:
            num = num * 26 + (ord(c) - ord('a') + 1)
        return num

    
    bans = [to_num(ban) for ban in bans]
    bans.sort()

    # 2. n번째 주문을 찾으면서, 앞에서 봉인된 주문을 만나면 그만큼 뒤로 밀어준다.
    for ban in bans:
        if ban <= n:
            n += 1
        else:
            break

    # 3. 숫자(n)를 다시 주문 문자열로 변환
    answer = ''

    while n > 0:
        n -= 1
        answer = chr(n % 26 + ord('a')) + answer
        n //= 26
    return answer