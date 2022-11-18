# 문제 링크: https://www.acmicpc.net/problem/9094

import sys
input = sys.stdin.readline

result = [[0 for _ in range(101)] for _ in range(101)]
for b in range(2, 100):
    for m in range(1, 101):
        result[b][m] = result[b - 1][m]
        for a in range(1, b):
            if (a * a + b * b + m) % (a * b) == 0:
                result[b][m] += 1

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(result[n - 1][m])
