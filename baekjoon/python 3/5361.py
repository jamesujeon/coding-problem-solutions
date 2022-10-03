# 문제 링크: https://www.acmicpc.net/problem/5361

import sys
input = sys.stdin.readline

prices = [350.34, 230.90, 190.55, 125.30, 180.90]

for _ in range(int(input())):
    counts = map(int, input().split())

    print(f'${sum(price * count for price, count in zip(prices, counts)):.2f}')
