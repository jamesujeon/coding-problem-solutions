# 문제 링크: https://www.acmicpc.net/problem/9550

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    _, K = map(int, input().split())

    print(sum(i // K for i in map(int, input().split())))
