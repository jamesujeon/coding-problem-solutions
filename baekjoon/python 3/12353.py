# 문제 링크: https://www.acmicpc.net/problem/12353

import sys
input = sys.stdin.readline

for x in range(1, int(input()) + 1):
    s, m, f = input().split()
    mf, mi = map(int, m[:-1].split("'"))
    ff, fi = map(int, f[:-1].split("'"))

    m, f = mf * 12 + mi, ff * 12 + fi
    a = (m + f + (5 if s == 'B' else -5)) / 2
    a, b = int(a - 4 + (.5 if a % 2 else 0)), int(a + 4)

    print(f"Case #{x}: {a // 12}'{a % 12}\" to {b // 12}'{b % 12}\"")
