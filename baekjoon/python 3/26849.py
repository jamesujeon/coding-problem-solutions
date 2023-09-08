# 문제 링크: https://www.acmicpc.net/problem/26849

import sys
input = sys.stdin.readline

v = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    v.append(a / b)

print(min(v), max(v), sum(v))
