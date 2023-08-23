# 문제 링크: https://www.acmicpc.net/problem/26392

import sys
input = sys.stdin.readline

n, r, s = map(int, input().split())
for _ in range(n):
    v = [r - i for i in range(r) for ch in input() if ch == '#']
    print(max(v) - min(v))
