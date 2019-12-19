# 문제 링크: http://codeforces.com/problemset/problem/580/A

_ = input()
nums = list(map(int, input().split()))

max_len = sub_len = prev_num = 0
for num in nums:
  sub_len = sub_len + 1 if prev_num <= num else 1
  max_len = max(max_len, sub_len)
  prev_num = num

print(max_len)