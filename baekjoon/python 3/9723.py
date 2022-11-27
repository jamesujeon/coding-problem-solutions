# 문제 링크: https://www.acmicpc.net/problem/9723

import sys
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    a, b, c = sorted(map(int, input().split()))

    print(f"Case #{i}: {'YES' if c * c == a * a + b * b else 'NO'}")
