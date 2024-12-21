# 문제 링크: https://www.acmicpc.net/problem/15279

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    b, p = map(float, input().split())

    d = 60 / p
    bpm = b * d

    print(f"{bpm - d:.4f} {bpm:.4f} {bpm + d:.4f}")
