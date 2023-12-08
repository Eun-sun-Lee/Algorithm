import sys
str = sys.stdin.readline().strip()
ans = 0
cnt = 1

for i in range(len(str) - 1, -1, -1):
    if str[i] == 'A':
        ans = ans + (cnt * 10)
    elif str[i] == 'B':
        ans += (cnt * 11)
    elif str[i] == 'C':
        ans += (cnt * 12)
    elif str[i] == 'D':
        ans += (cnt * 13)
    elif str[i] == 'E':
        ans += (cnt * 14)
    elif str[i] == 'F':
        ans += (cnt * 15)
    else:
        ans += (cnt * int(str[i]))
    cnt *= 16
print(ans)