# 문제 링크: https://www.acmicpc.net/problem/5086

import sys
input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    if not a and not b:
        break

    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')