# 문제 링크: https://www.acmicpc.net/problem/13280

import sys
input = sys.stdin.readline

while (n := int(input())) != 0:
    a = sorted(map(int, input().split()))
    print(min(a[i + 1] - a[i] for i in range(n - 1)))
