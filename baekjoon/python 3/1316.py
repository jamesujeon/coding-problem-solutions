# 문제 링크: https://www.acmicpc.net/problem/1316

import sys

def check(s):
  i, l = 0, []
  while i < len(s):
    if s[i] in l:
      return False
    l.append(s[i])
    j = i + 1
    while j < len(s) and s[i] == s[j]:
      j += 1
    i = j
  return True

input()
print(sum(check(s) for s in sys.stdin))