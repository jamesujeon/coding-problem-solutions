# 문제 링크: https://www.acmicpc.net/problem/4583

import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    if s == '#':
        break

    result = ''
    for c in s[::-1]:
        if c in 'bdpq':
            result += {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}[c]
        elif c in 'iovwx':
            result += c
        else:
            result = 'INVALID'
            break

    print(result)
