# 문제 링크: https://www.acmicpc.net/problem/14790

for x in range(1, int(input()) + 1):
    n = int(input())
    while int(''.join(sorted(str(n)))) != n:
        n -= 1

    print(f"Case #{x}: {n}")
