# 문제 링크: https://www.acmicpc.net/problem/15239

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    _, s = input(), input().strip()

    v = (
        any(i.islower() for i in s) and
        any(i.isupper() for i in s) and
        any(i.isdigit() for i in s) and
        any(i in set('+_)(*&^%$#@!./,;{}') for i in s) and
        len(s) > 11
    )

    print(['invalid', 'valid'][v])
