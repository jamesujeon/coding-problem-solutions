# 문제 링크: https://www.acmicpc.net/problem/5176

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    P, _ = map(int, input().split())
    print(P - len({int(input()) for _ in range(P)}))
