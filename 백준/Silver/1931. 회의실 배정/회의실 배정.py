# 회의의 최대 갯수 기준
import sys
n = int(sys.stdin.readline())
meeting = n * []
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meeting.append((start, end))

def ans(meeting, n):
    meeting = sorted(meeting, key = lambda x : (x[1], x[0]))
    # print(meeting)
    meet = []
    meet.append(meeting[0][1])
    for i in range(1, n):
        if meeting[i][0] >= meet[-1]:
            meet.append(meeting[i][1])
    print(len(meet))
ans(meeting, n)