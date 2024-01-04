import sys

n = int(sys.stdin.readline())
num_set = set()

for _ in range(n):
    command_line = sys.stdin.readline().split()
    command = command_line[0]
    num = ""
    if len(command_line) == 2:
        num = int(command_line[1])

    if command == "add":
        num_set.add(num)
    elif command == "remove":
        num_set.discard(num)
    elif command == "check":
        print(1 if num in num_set else 0)
    elif command == "toggle":
        if num in num_set:
            num_set.discard(num)
        else:
            num_set.add(num)
    elif command == "all":
        num_set = set(range(1, 21))
    elif command == "empty":
        num_set = set()

# 출력 방식 변경
# sys.stdout.write('\n'.join(map(str, [1 if i in num_set else 0 for i in range(1, 21)])))