# 문제 링크: https://www.acmicpc.net/problem/23663

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    input(), input()

    print("Yes" if n <= m else "No")
