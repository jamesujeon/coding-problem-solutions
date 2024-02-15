# 문제 링크: https://www.acmicpc.net/problem/4974

import sys
input = sys.stdin.readline

while (n := int(input())) != 0:
    s = sorted(int(input()) for _ in range(n))

    print(sum(s[1:-1]) // (n - 2))
