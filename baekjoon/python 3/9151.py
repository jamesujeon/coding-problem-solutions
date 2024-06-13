# 문제 링크: https://www.acmicpc.net/problem/9151

import sys
input = sys.stdin.readline

c = [i**3 for i in range(54)]
t = [i * (i + 1) * (i + 2) // 6 for i in range(96)]

while (n := int(input())) != 0:
    print(max(i + j for i in c for j in t if i + j <= n))
