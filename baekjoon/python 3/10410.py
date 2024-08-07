# 문제 링크: https://www.acmicpc.net/problem/10410

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, s, b, c = input().split()

    result = 'ineligible'
    if s >= '2010/01/01' or b >= '1991/01/01':
        result = 'eligible'
    elif int(c) < 41:
        result = 'coach petitions'

    print(n, result)
