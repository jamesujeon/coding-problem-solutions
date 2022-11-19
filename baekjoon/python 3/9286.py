# 문제 링크: https://www.acmicpc.net/problem/9286

import sys
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    print(f"Case {i}:")
    for _ in range(int(input())):
        num = int(input()) + 1
        if num <= 6:
            print(num)
