# 문제 링크: https://www.acmicpc.net/problem/6060

import sys
input = sys.stdin.readline

R = 0
for _, _, C in sorted(list(map(int, input().split())) for _ in range(int(input()) - 1)):
    R ^= C

print(R)
