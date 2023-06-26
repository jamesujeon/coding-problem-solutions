# 문제 링크: https://www.acmicpc.net/problem/24830

import sys
input = sys.stdin.readline

result = 1
for _ in range(int(input())):
    a, op, b = input().split()
    a, b = int(a), int(b)

    if op == '+':
        result = a + b - result
    elif op == '-':
        result *= a - b
    elif op == '*':
        result = (a * b)**2
    else:
        result = (a + 1) // 2

    print(result)
