# 문제 링크: https://www.acmicpc.net/problem/23348

import sys
input = sys.stdin.readline

result = 0
A, B, C = map(int, input().split())
for _ in range(int(input())):
    score = 0
    for _ in range(3):
        a, b, c = map(int, input().split())
        score += a * A + b * B + c * C
    result = max(score, result)

print(result)
