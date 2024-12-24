# 문제 링크: https://www.acmicpc.net/problem/15406

import sys
input = sys.stdin.readline

t = 0
while (s := input().strip()) != 'TOTAL':
    p, c = map(int, input().split())
    t += p * c

print(["PAY", "PROTEST"][int(input()) > t])
