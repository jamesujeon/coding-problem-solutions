# 문제 링크: https://www.acmicpc.net/problem/1934

import sys
input = sys.stdin.readline

def lcm(a: int, b: int) -> int:
    lcm = a * b
    while a % b > 0:
        a, b = b, a % b
    return lcm // b

lcms = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    lcms.append(lcm(a, b))

print(*lcms, sep='\n')