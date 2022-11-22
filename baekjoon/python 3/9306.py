# 문제 링크: https://www.acmicpc.net/problem/9306

import sys
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    f, l = input().rstrip(), input().rstrip()

    print(f"Case {i}: {l}, {f}")
