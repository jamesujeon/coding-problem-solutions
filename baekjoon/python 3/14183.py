# 문제 링크: https://www.acmicpc.net/problem/14183

import sys
input = sys.stdin.readline

while (s := input().strip()) != '0 0':
    m, n = map(int, s.split())
    c = list(map(int, input().split()))
    print(sum(all(i >= j for i, j in zip(c, list(map(int, input().split())))) for _ in range(n)))
