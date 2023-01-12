# 문제 링크: https://www.acmicpc.net/problem/11134

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, C = map(int, input().split())

    print(N // C + int(N % C > 0))
