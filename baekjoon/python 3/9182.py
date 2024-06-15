# 문제 링크: https://www.acmicpc.net/problem/9182

import sys
input = sys.stdin.readline

x = 1
while (s := input().strip()) != "-1 -1 -1 -1":
    p, e, i, d = map(int, s.split())

    y = d + 1
    while y < 21252 and (y % 23 != p % 23 or y % 28 != e % 28 or y % 33 != i % 33):
        y += 1
    y -= d

    print(f"Case {x}: the next triple peak occurs in {y} days.")
    x += 1
