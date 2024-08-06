import sys 
t = int(sys.stdin.readline())
MAX = 1000000
devisors = [1] * (MAX + 1) # 약수의 합 
dp = [0] * (MAX + 1) 
dp[1] = 1


def sol():
    for i in range(2, MAX + 1):
        j = 1
        while i * j <= MAX:
            devisors[i * j] += i
            j += 1
    # print(devisors[:10])

    for i in range(2, MAX + 1):
        dp[i] = dp[i - 1] + devisors[i]
    # print(dp[:10])

sol()
for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[n])