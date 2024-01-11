# 문제 링크: https://www.acmicpc.net/problem/4592

import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    if s == '0':
        break

    n = list(map(int, s.split()))
    prev = None
    for i in range(1, n[0] + 1):
        if n[i] != prev:
            print(n[i], end=' ')
        prev = n[i]
    print('$')
