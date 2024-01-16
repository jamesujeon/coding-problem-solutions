# 문제 링크: https://www.acmicpc.net/problem/4285

import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    if s == '0':
        break

    k, m = map(int, s.split())
    k = set(input().split())
    meets = True
    for _ in range(m):
        _, r, *c = input().split()
        if sum(n in k for n in c) < int(r):
            meets = False

    print('yes' if meets else 'no')
