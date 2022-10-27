# 문제 링크: https://www.acmicpc.net/problem/5607

import sys
input = sys.stdin.readline

a = b = 0
for _ in range(int(input())):
    c1, c2 = map(int, input().split())
    if c1 > c2:
        a += c1 + c2
    elif c1 < c2:
        b += c1 + c2
    else:
        a += c1
        b += c2

print(a, b)
