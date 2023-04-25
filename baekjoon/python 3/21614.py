# 문제 링크: https://www.acmicpc.net/problem/21614

import sys

d = None
for input in sys.stdin:
    i = input.strip()
    if i == "99999":
        break

    s = sum(map(int, i[:2]))
    if s > 0:
        d = ("right", "left")[s % 2]

    print(d, i[2:])
