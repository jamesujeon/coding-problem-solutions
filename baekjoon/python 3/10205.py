# 문제 링크: https://www.acmicpc.net/problem/10205

import sys
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    h, a = int(input()), input()

    print(f"Data Set {i}:")
    print(h + a.count('c') - a.count('b'))
    print()
