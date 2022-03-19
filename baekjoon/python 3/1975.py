# 문제 링크: https://www.acmicpc.net/problem/1975

import sys
input = sys.stdin.readline

def f(N: int, b: int) -> int:
    count = 0
    while N % b == 0:
        count += 1
        N //= b
    return count

result = [0] * 1001
for N in range(2, 1001):
    result[N] = sum(f(N, b) for b in range(2, N + 1))

for _ in range(int(input())):
    print(result[int(input())])
