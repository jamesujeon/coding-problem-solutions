# 문제 링크: https://www.acmicpc.net/problem/10834

import sys
input = sys.stdin.readline

r1, r2 = 0, 1
for _ in range(int(input())):
    a, b, s = map(int, input().split())
    if s:
        r1 = 1 - r1
    r2 = int(r2 / a) * b

print(r1, r2)
