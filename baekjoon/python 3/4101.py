# 문제 링크: https://www.acmicpc.net/problem/4101

import sys

for input in sys.stdin:
    a, b = map(int, input.split())
    if a == b == 0:
        break

    print("Yes" if a > b else "No")
