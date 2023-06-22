# 문제 링크: https://www.acmicpc.net/problem/24783

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c = map(int, input().split())

    print("Possible" if c in (a + b, abs(a - b), a * b, a / b, b / a) else "Impossible")
