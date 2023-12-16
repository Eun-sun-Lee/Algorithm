import sys
n, weight = map(int, sys.stdin.readline().split())
w = [0] * n
price = [0] * n
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    w[i] = a
    price[i] = b
def bag(n, weight, w, price):
    dp = [0] * (weight + 1)
    for i in range(n):
        for j in range(weight, w[i] - 1, -1): # 한번 쓴건 또 못쓰도록
            dp[j] = max(dp[j], dp[j - w[i]] + price[i])
        print(dp)
    # 원래 짰던 코드
    # for i in range(1, weight + 1):
    #     maxPrice = 0
    #     for j in range(n):
    #         if i - w[j] < 0: continue
    #         maxPrice = max(maxPrice, dp[i - w[j]] + price[j])
    #     dp[i] = maxPrice
    print(dp[weight])
bag(n, weight, w, price)