# 문제 링크: https://www.acmicpc.net/problem/25024

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())

    days = 31
    if x == 2:
        days = 29
    elif x in (4, 6, 9, 11):
        days = 30

    print(f"{'Yes' if x < 24 and y < 60 else 'No'} {'Yes' if 0 < x < 13 and 0 < y <= days else 'No'}")
