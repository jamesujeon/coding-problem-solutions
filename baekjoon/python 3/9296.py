# 문제 링크: https://www.acmicpc.net/problem/9296

import sys
input = sys.stdin.readline

for i in range(int(input())):
    input()
    print(f"Case {i + 1}: {sum(a != b for a, b in zip(input(), input()))}")
