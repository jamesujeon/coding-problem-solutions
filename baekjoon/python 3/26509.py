# 문제 링크: https://www.acmicpc.net/problem/26509

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))

    print("YES" if a == b and a[0] * a[0] + a[1] * a[1] == a[2] * a[2] else "NO")
