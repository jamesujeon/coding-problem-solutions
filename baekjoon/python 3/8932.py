# 문제 링크: https://www.acmicpc.net/problem/8932

import sys
input = sys.stdin.readline

constants = [
    (9.23076, 26.7, 1.835),
    (1.84523, 75, 1.348),
    (56.0211, 1.5, 1.05),
    (4.99087, 42.5, 1.81),
    (0.188807, 210, 1.41),
    (15.9803, 3.8, 1.04),
    (0.11193, 254, 1.88)
]

for _ in range(int(input())):
    print(sum(int(c[0] * (abs(c[1] - s) ** c[2])) for c, s in zip(constants, map(int, input().split()))))
