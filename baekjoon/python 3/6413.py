# 문제 링크: https://www.acmicpc.net/problem/6413

import sys
input = sys.stdin.readline

while (s := input().strip()) != '#':
    d = {r: [] for r in 'A23456789TJQK'}
    for i, c in enumerate(s.split() + sum((input().split() for _ in range(3)), [])):
        d['KQJT98765432A'[i % 13]].insert(0, c)

    c = d['K'].pop()
    while d[c[0]]:
        c = d[c[0]].pop()

    print(f'{52 - sum(map(len, d.values())):02d},{c}')
