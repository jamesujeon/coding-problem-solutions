# 문제 링크: https://www.acmicpc.net/problem/4890

import sys
input = sys.stdin.readline

while (s := input().strip()) != '0 0':
    w, h = map(int, s.split())
    if w < h:
        w, h = h, w

    print(w * h if w % h else w // h)
