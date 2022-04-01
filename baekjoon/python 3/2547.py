# 문제 링크: https://www.acmicpc.net/problem/2547

import sys
input = sys.stdin.readline

results = []
for _ in range(int(input())):
    _, n = input(), int(input())
    count = sum(int(input()) for _ in range(n))

    results.append('YES' if count % n == 0 else 'NO')

for result in results:
    print(result)
