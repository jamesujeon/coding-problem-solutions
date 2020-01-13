# 문제 링크: https://www.acmicpc.net/problem/1912

import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))

sums = [nums[0]]
for i in range(1, n):
  sums.append(sums[i - 1] + nums[i] if sums[i - 1] + nums[i] > nums[i] else nums[i])

print(max(sums))




# 10 6 9 10 15 21 -14 12 33 32





# 10, -4, 3, 1, 5, 6, -35, 12, 21, -1

# 7 8 -4 -1 => 7 + 8 = 15

# 7 8 -4 -1 10
# 7 15 11 10 20



# 7 + 8 = 15
# 7 + 8 + (-4) + (-1) + 10 = 20


# 7 8 -4 -1 10 => 15 -5 10