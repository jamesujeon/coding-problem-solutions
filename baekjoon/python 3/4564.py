# 문제 링크: https://www.acmicpc.net/problem/4564

import sys
input = sys.stdin.readline

while True:
    S = input().strip()
    if S == '0':
        break

    result = [S]
    while len(S) > 1:
        n = 1
        for i in S:
            n *= int(i)
        S = str(n)
        result.append(S)

    print(*result)
