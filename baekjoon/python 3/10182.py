# 문제 링크: https://www.acmicpc.net/problem/10182

from math import log10

for _ in range(int(input())):
    v, d = input().split(' = ')
    d = -log10(float(d))
    if 'O' in v:
        d = 14 - d

    print(f"{d:.2f}")
