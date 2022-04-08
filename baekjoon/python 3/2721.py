# 문제 링크: https://www.acmicpc.net/problem/2721

import sys
input = sys.stdin.readline

results = []
for _ in range(int(input())):
    n = int(input())
    results.append(sum(k * (k + 1) * (k + 2) // 2 for k in range(1, n + 1)))

for result in results:
    print(result)
