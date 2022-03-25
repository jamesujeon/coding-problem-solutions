# 문제 링크: https://www.acmicpc.net/problem/2460

nums = [map(int, input().split()) for _ in range(10)]

nums = [0] + [b - a for a, b in nums]
for i in range(1, len(nums)):
    nums[i] += nums[i - 1]

print(max(nums))
