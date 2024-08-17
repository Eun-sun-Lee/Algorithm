import sys 
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = []

    for _ in range(n):
        num = str(sys.stdin.readline())
        arr.append(num)

    arr.sort()

    def sol(n, arr):
        phone_num = set()

        for num in arr:
            prefix = ""
            for i in range(len(num) - 1):
                prefix += num[i]
                # print(prefix)
                if prefix in phone_num:
                    print("NO")
                    return 
            phone_num.add(prefix)
        print("YES")
    sol(n, arr)