# 문제 링크: https://www.acmicpc.net/problem/14648

import sys
input = lambda: map(int, sys.stdin.readline().split())

n, q = input()
s = list(input())
for _ in range(q):
    q1, *q2 = input()
    if q1 == 1:
        a, b = q2
        print(sum(s[a - 1:b]))
        s[a - 1], s[b - 1] = s[b - 1], s[a - 1]
    else:
        a, b, c, d = q2
        print(sum(s[a - 1:b]) - sum(s[c - 1:d]))
