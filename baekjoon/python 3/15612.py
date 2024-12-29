# 문제 링크: https://www.acmicpc.net/problem/15612

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    v = int(input())

    s = ''
    while v > 0:
        s += str(v % 3)
        v //= 3

    print(s[::-1] if s else 0)
