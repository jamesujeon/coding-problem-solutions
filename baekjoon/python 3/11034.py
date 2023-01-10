# 문제 링크: https://www.acmicpc.net/problem/11034

import sys

for l in sys.stdin.readlines():
    A, B, C = sorted(map(int, l.split()))

    print(max(B - A, C - B) - 1)
