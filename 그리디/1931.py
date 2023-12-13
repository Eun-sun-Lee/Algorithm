import sys
n = int(sys.stdin.readline())
time = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    time.append((start,end))
time = sorted(time, key=lambda x: (x[1], x[0])) # 빨리 끝나는 순서대로, 빨리 끝나는 시간이 같다면 빨리 시작하는 기준으로 정렬

def meeting(n, time):
    meet = []
    meet.append(time[0][1])
    for i in range(1,n):
        if meet[-1] <= time[i][0]:
            meet.append(time[i][1])
    print(len(meet))
    # print(meet)
meeting(n, time)
