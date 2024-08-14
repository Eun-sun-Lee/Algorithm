import sys

n, k = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))

# 차이 배열을 구합니다.
diff = []
for i in range(1, n):
    diff.append(heights[i] - heights[i - 1])

# 차이 배열을 오름차순으로 정렬합니다.
diff.sort()

# 상위 (n-k)개의 차이만을 사용하면 됩니다.
# 그 차이들의 합이 최소화된 비용이 됩니다.
result = sum(diff[:n-k])

print(result)
