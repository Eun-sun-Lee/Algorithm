N = int(input())
guest_list = list(map(int, input().split()))

limit = int(input())
val = sum(guest_list[:limit])
guest_sum = [val]

for i in range(N-limit) :
  val += guest_list[i+limit] - guest_list[i]
  guest_sum.append(val)

dp = [[0]*(4) for _ in range(N+1)]
for i in range(1, N+1) :
  for j in range(3) :
    dp[i][j] = dp[i-1][j]
    if i >= limit :
      dp[i][j] = max(dp[i][j], dp[i-limit][j+1] + guest_sum[i-limit])

print(dp[-1][0])