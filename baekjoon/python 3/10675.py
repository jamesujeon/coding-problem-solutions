# 문제 링크: https://www.acmicpc.net/problem/10675

import sys
input = sys.stdin.readline

A, B, N = map(int, input().split())
min_c = -1
for _ in range(N):
    c, _ = map(int, input().split())
    if [i for i in map(int, input().split()) if i in [A, B]] == [A, B]:
        min_c = min(c, min_c) if min_c > -1 else c

print(min_c)
