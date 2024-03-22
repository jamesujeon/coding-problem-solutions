# 문제 링크: https://www.acmicpc.net/problem/5768

import sys
input = sys.stdin.readline

while (s := input().strip()) != '0 0':
    M, N = map(int, s.split())

    X = Y = 0
    for i in range(M, N + 1):
        d = 0
        for j in range(1, int(i ** .5) + 1):
            if i % j == 0:
                d += 1
                if i != j * j:
                    d += 1
        if d >= Y:
            X, Y = i, d

    print(X, Y)
