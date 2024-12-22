# 문제 링크: https://www.acmicpc.net/problem/15296

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k, b, n = map(int, input().split())

    s = 0
    while n > 0:
        s += (n % b)**2
        n //= b

    print(k, s)
