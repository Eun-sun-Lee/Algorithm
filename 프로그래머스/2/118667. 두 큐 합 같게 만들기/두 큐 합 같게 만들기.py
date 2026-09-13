from collections import deque

def solution(queue1, queue2):
    answer = -1

    total = sum(queue1) + sum(queue2)

    # 예외처리
    if total % 2 != 0:
        return -1

    target = total // 2

    q1 = deque(queue1)
    q2 = deque(queue2)

    sum_1 = sum(queue1)

    cnt = 0
    max_cnt = (len(queue1) + len(queue2)) * 2

    while cnt < max_cnt:

        if sum_1 == target:
            return cnt

        if sum_1 > target:
            num = q1.popleft()
            sum_1 -= num
            q2.append(num)

        else:
            num = q2.popleft()
            sum_1 += num
            q1.append(num)

        cnt += 1

    return -1