# 문제 링크: https://www.acmicpc.net/problem/9838

import sys
input = sys.stdin.readline

n = int(input())
gifts = [0] * n
for i in range(n):
    gifts[int(input()) - 1] = i + 1

for gift in gifts:
    print(gift)
