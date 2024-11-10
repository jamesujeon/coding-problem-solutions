# 문제 링크: https://www.acmicpc.net/problem/14561

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A, n = map(int, input().split())

    a = ''
    while A > 0:
        a += '0123456789ABCDEF'[A % n]
        A //= n

    print(int(a == a[::-1]))
