# 문제 링크: https://www.acmicpc.net/problem/9950

import sys

for input in sys.stdin:
    l, w, a = map(int, input.split())
    if l + w + a == 0:
        break

    if l == 0:
        l = a // w
    elif w == 0:
        w = a // l
    elif a == 0:
        a = l * w

    print(l, w, a)
