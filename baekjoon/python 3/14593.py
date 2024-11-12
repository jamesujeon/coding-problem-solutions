# 문제 링크: https://www.acmicpc.net/problem/14593

import sys
input = sys.stdin.readline

N = []
for i in range(int(input())):
    S, C, L = map(int, input().split())
    N.append((-S, C, L, i + 1))

print(sorted(N)[0][3])
