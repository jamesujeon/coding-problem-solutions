# 문제 링크: https://www.acmicpc.net/problem/1362

import sys
input = sys.stdin.readline

i = 0
while True:
    o, w = map(int, input().split())
    if o == w == 0:
        break

    while True:
        a, n = input().split()
        if a == '#':
            break
        if w > 0:
            w += int(n) * (1 if a == 'F' else -1)

    i += 1
    result = "RIP"
    if o / 2 < w < o * 2:
        result = ":-)"
    elif w > 0:
        result = ":-("

    print(i, result)
