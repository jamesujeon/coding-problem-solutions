# 문제 링크: http://codeforces.com/problemset/problem/580/A

_ = input()
nums = list(map(int, input().split()))

max_len = i = 0
while i < len(nums):
  current = nums[i]

  sub_len = 1
  for j in range(i + 1, len(nums)):
    if current > nums[j]:
      break

    current = nums[j]
    sub_len += 1

  max_len = max(max_len, sub_len)
  i += sub_len

print(max_len)