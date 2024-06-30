# 문제 링크: https://www.acmicpc.net/problem/9777

import sys
input = sys.stdin.readline

d = [0] * 12
for _ in range(int(input())):
    d[int(input().split('/')[1]) - 1] += 1

for i in range(12):
    print(i + 1, d[i])
