# 문제 링크: https://www.acmicpc.net/problem/3183

import sys
input = sys.stdin.readline

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    d, m, y = map(int, input().split())
    if d == m == y == 0:
        break

    if 1 <= m <= 12 and 1 <= d <= (days[m] + int(m == 2 and ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0))):
        print('Valid')
    else:
        print('Invalid')
