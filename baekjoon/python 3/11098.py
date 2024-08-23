# 문제 링크: https://www.acmicpc.net/problem/11098

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    print(sorted([input().split() for _ in range(int(input()))], key=lambda x: int(x[0]))[-1][1])
