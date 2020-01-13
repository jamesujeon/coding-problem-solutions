# 문제 링크: https://www.acmicpc.net/problem/1912

import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))

sums = [nums[0]]
for i in range(1, n):
  sums.append(sums[i - 1] + nums[i] if sums[i - 1] + nums[i] > nums[i] else nums[i])

print(max(sums))