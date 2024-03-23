# 문제 링크: https://www.acmicpc.net/problem/5919

import sys
input = sys.stdin.readline

p = [int(input()) for _ in range(int(input()))]
h = sum(p) // len(p)
h = sum(abs(h - i) for i in p) // 2

print(h)
