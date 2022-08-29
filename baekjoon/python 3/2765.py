# 문제 링크: https://www.acmicpc.net/problem/2765

import sys
from math import pi

i = 0
for input in sys.stdin:
    d, r, s = map(float, input.split())
    if r == 0:
        break

    distance = d * r * pi / 63360
    mph = distance / s * 3600

    i += 1
    print(f"Trip #{i}: {distance:.2f} {mph:.2f}")
