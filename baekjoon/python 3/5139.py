# 문제 링크: https://www.acmicpc.net/problem/5139

import sys
input = sys.stdin.readline

for k in range(1, int(input()) + 1):
    h, w = map(int, input().split())

    d = []
    for c in zip(*[input().strip() for _ in range(h)]):
        if 'X' not in c:
            d.append('N')
            continue

        cost = 0
        for i in c:    
            if i == 'X':
                break
            cost += 3 if i == 'H' else 1
        d.append(str(cost))

    print(f'Data Set {k}:\n{" ".join(d)}\n')
