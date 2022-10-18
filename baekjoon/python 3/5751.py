# 문제 링크: https://www.acmicpc.net/problem/5751

import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break

    zeros = input().count('0')
    print(f'Mary won {zeros} times and John won {N - zeros} times')
