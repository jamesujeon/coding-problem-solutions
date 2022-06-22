# 문제 링크: https://www.acmicpc.net/problem/16693

from math import pi

A1, P1 = map(int, input().split())
R1, P2 = map(int, input().split())

print('Slice of pizza' if A1 / P1 > R1**2 * pi / P2 else 'Whole pizza')
