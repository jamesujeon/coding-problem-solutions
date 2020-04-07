# 문제 링크: https://www.acmicpc.net/problem/1316

import sys

input()
print(sum(list(s) == sorted(s, key=s.find) for s in sys.stdin))