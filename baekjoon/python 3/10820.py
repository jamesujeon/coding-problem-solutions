# 문제 링크: https://www.acmicpc.net/problem/10820

import sys

for s in sys.stdin:
    c = [0] * 4
    for i in s[:-1]:
        c[i.isupper() + (2 if i.isdigit() else 0) + (3 if i.isspace() else 0)] += 1

    print(*c)
