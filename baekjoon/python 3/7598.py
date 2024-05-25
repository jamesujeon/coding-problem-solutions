# 문제 링크: https://www.acmicpc.net/problem/7598

import sys
input = sys.stdin.readline

while (s := input().strip()) != '# 0':
    f, n = s.split()

    n = int(n)
    while (t := input().strip()) != 'X 0':
        t, m = t[0], int(t[2:])
        if t == 'B' and n + m <= 68:
            n += m
        elif t == 'C' and n - m >= 0:
            n -= m

    print(f, n)
