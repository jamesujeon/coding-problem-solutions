# 문제 링크: https://www.acmicpc.net/problem/22061

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c = map(int, input().split())

    print(("YES", "NO")[c > min(b, c // 2) * 2 + a])
