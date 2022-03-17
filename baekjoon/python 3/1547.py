# 문제 링크: https://www.acmicpc.net/problem/1547

import sys
input = sys.stdin.readline

cups = list(range(4))
for _ in range(int(input())):
    x, y = map(int, input().split())
    cups[x], cups[y] = cups[y], cups[x]

print(cups.index(1))
