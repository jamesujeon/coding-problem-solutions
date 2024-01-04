# 문제 링크: https://www.acmicpc.net/problem/4447

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    c = s.lower().count('g') - s.lower().count('b')

    result = 'NEUTRAL'
    if c > 0:
        result = "GOOD"
    elif c < 0:
        result = "A BADDY"

    print(f'{s} is {result}')
