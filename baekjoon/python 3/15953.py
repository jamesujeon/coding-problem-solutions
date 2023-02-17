# 문제 링크: https://www.acmicpc.net/problem/15953

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())

    result = 0
    if 0 < a < 22:
        for i in range(1, 7):
            if a <= i * (i + 1) // 2:
                result += [500, 300, 200, 50, 30, 10][i - 1]
                break
    if 0 < b < 32:
        for i in range(1, 6):
            if b <= 2**i - 1:
                result += 2**(10 - i)
                break

    print(result * 10000)
