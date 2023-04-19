# 문제 링크: https://www.acmicpc.net/problem/21280

N = int(input())
nums = list(map(int, input().split()))

results = [0, 0]
for i in range(1, N):
    diff = nums[i] - nums[i - 1]
    results[diff > 0] += abs(diff)

print(results[0], results[1])
