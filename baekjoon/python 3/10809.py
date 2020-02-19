# 문제 링크: https://www.acmicpc.net/problem/10809

import string

s = input()
for c in string.ascii_lowercase:
  print(s.find(c), end=' ')