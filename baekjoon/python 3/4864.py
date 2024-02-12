# 문제 링크: https://www.acmicpc.net/problem/4864

import sys
input = sys.stdin.readline

c = [0]
for i in range(1, 143):
    for j in range(i):
        c.append(c[-1] + i)

while (n := int(input())) != 0:
    print(n, c[n])
