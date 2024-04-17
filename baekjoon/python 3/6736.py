# 문제 링크: https://www.acmicpc.net/problem/6736

import sys
input = sys.stdin.readline

f = [1]
for i in range(2, 367):
    f.append(f[-1] * i)

for _ in range(int(input())):
    a, b = input().split()

    print(str(f[int(a) - 1]).count(b))
