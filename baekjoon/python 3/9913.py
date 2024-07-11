# 문제 링크: https://www.acmicpc.net/problem/9913

import sys
input = sys.stdin.readline

d = {}
for _ in range(int(input())):
    n = int(input())
    d[n] = d.get(n, 0) + 1

print(max(d.values()))
