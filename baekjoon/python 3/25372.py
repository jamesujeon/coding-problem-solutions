# 문제 링크: https://www.acmicpc.net/problem/25372

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    print(("no", "yes")[6 <= len(input().strip()) <= 9])
