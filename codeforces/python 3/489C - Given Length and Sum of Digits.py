# 문제 링크: http://codeforces.com/problemset/problem/489/C

m, s = map(int, input().split())

remainder_str = str(s % 9) if s % 9 > 0 else ''
min_num = remainder_str + '9' * (s // 9)
max_num = '9' * (s // 9) + remainder_str

if len(min_num) == 0:
  min_num = max_num = 0 if m == 1 else -1
elif len(min_num) > m:
  min_num = max_num = -1
elif len(min_num) < m:
  min_num = '1' + '0' * (m - len(min_num) - 1) + str(int(min_num[0]) - 1) + min_num[1:]
  max_num = max_num + '0' * (m - len(max_num))

print(min_num, max_num)