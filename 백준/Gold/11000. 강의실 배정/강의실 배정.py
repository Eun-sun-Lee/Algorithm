import sys
import heapq

n = int(sys.stdin.readline())
lectureH = []
lecture = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    heapq.heappush(lectureH, (a, b))  

end_times = []
ans = 0

while lectureH:
    start, end = heapq.heappop(lectureH)

    # 현재 진행 중인 강의 중에서 끝난 강의는 제거
    while end_times and end_times[0] <= start:
        heapq.heappop(end_times)

    # 현재 강의의 종료 시간을 추가
    heapq.heappush(end_times, end)

    # 동시에 진행 중인 강의 수의 최대값 갱신
    ans = max(ans, len(end_times))

print(ans)
