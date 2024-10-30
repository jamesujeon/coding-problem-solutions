# 문제 링크: https://www.acmicpc.net/problem/14290

import sys
input = sys.stdin.readline

for t in range(1, int(input()) + 1):
    s = input().strip()
    i, j = map(lambda x: int(x) - 1, input().split())
    k = len(s)

    print(f"Case #{t}: {s.count('B') * (j // k - i // k - 1) + s[i % k:].count('B') + s[:j % k + 1].count('B')}")
