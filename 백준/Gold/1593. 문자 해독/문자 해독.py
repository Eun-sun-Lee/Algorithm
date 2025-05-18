import sys

lenW, lenS = map(int, sys.stdin.readline().split())
w = list(str(sys.stdin.readline().strip()))
s = str(sys.stdin.readline().strip())

wl = [0] * 58
sl = [0] * 58

answer = 0

for i in w:
    wl[ord(i)-65] += 1


def solution():
    global answer 
    length = 0

    for i in range(lenS):
        sl[ord(s[i])-65] += 1
        length += 1

        if length == lenW:
            if wl == sl:
                answer += 1

            length -= 1
            sl[ord(s[i+1-lenW])-65] -= 1


solution()
print(answer)

