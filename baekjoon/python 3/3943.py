# 문제 링크: https://www.acmicpc.net/problem/3943

import sys
input = sys.stdin.readline

max_n = {1: 1}
def get_max_n(n):
    if n in max_n:
        return max_n[n]
    max_n[n] = max(n, get_max_n(n * 3 + 1 if n % 2 else n // 2))
    return max_n[n]

for _ in range(int(input())):
    print(get_max_n(int(input())))
