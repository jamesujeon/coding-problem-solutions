# 문제 링크: https://www.acmicpc.net/problem/21200

import sys
input = sys.stdin.readline

N, P, S = map(int, input().split())
for _ in range(S):
    print("KEEP" if P in list(map(int, input().split()))[1:] else "REMOVE")
