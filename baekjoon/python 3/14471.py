# 문제 링크: https://www.acmicpc.net/problem/14471

import sys
input = lambda: map(int, sys.stdin.readline().split())

n, m = input()
p = []
for _ in range(m):
    _, b = input()
    p.append(max(b - n, 0))

print(sum(sorted(p)[:-1]))
