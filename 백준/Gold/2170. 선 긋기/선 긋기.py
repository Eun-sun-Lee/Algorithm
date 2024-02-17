import sys
n = int(sys.stdin.readline())
line = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    line.append((start, end))

line.sort()
# print(line)

last = -sys.maxsize
answer = 0

for start, end in line:
    if last > start:
        if last < end:
            # print("(end - last)", end - last)
            answer += (end - last)
            last = end
    else:
        # print("(end - start)", end - start)
        answer += (end - start)
        last = end

print(answer)