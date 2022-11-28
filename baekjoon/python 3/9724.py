# 문제 링크: https://www.acmicpc.net/problem/9724

from math import floor, ceil
import sys
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    A, B = map(int, input().split())

    print(f"Case #{i}: {floor(B**(1/3)) - ceil(A**(1/3)) + 1}")
