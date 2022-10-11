# 문제 링크: https://www.acmicpc.net/problem/5666

import sys

for l in sys.stdin.readlines():
    H, P = map(int, l.split())
    print(f'{H / P:.2f}')
