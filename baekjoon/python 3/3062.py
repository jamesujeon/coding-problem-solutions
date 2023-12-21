# 문제 링크: https://www.acmicpc.net/problem/3062

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = input()
    n = str(int(n) + int(n[::-1]))

    print('YES' if n == n[::-1] else 'NO')
