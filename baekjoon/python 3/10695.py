# 문제 링크: https://www.acmicpc.net/problem/10695

import sys
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    n, r1, c1, r2, c2 = map(int, input().split())

    print(f"Case {i}: {'YES' if sorted([abs(r1 - r2), abs(c1 - c2)]) == [1, 2] else 'NO'}")
