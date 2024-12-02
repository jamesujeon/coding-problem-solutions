# 문제 링크: https://www.acmicpc.net/problem/14969

import sys
input = sys.stdin.readline

while (s := input().strip()) != '0 0':
    n, m = map(int, s.split())
    a = sorted(map(int, input().split()))

    l, r = 0, n - 1
    max_s = 0
    while l < r:
        s = a[l] + a[r]
        if s <= m:
            max_s = max(s, max_s)
            l += 1
        else:
            r -= 1

    print(max_s if max_s else 'NONE')
