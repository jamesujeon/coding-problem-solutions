# 문제 링크: https://www.acmicpc.net/problem/9469

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, D, A, B, F = map(float, input().split())

    print(f"{int(N)} {D / (A + B) * F}")
