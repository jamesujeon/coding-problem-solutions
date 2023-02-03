# 문제 링크: https://www.acmicpc.net/problem/10698

import sys
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    X, O, Y, _, Z = input().split()

    print(f"Case {i}: {'YES' if eval(f'{X}{O}{Y}=={Z}') else 'NO'}")
