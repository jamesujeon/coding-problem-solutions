# 문제 링크: https://www.acmicpc.net/problem/9325

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = int(input())
    for _ in range(int(input())):
        q, p = map(int, input().split())
        s += q * p

    print(s)
