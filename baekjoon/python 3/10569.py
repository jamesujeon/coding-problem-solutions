# 문제 링크: https://www.acmicpc.net/problem/10569

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    V, E = map(int, input().split())

    print(2 - V + E)
