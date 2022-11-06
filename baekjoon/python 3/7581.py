# 문제 링크: https://www.acmicpc.net/problem/7581

import sys

for input in sys.stdin:
    l, w, h, v = map(int, input.split())
    if l + w + h + v == 0:
        break

    if l == 0:
        l = v // (w * h)
    elif w == 0:
        w = v // (l * h)
    elif h == 0:
        h = v // (l * w)
    else:
        v = l * w * h

    print(l, w, h, v)
