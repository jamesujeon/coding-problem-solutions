# 문제 링크: https://www.acmicpc.net/problem/5656

import sys
input = sys.stdin.readline

f = {
    '>': lambda x, y: x > y, '>=': lambda x, y: x >= y, '<': lambda x, y: x < y,
    '<=': lambda x, y: x <= y, '==': lambda x, y: x == y, '!=': lambda x, y: x != y
}

i = 1
while True:
    a, op, b = input().split()
    if op == 'E':
        break

    print(f'Case {i}: {str(f[op](int(a), int(b))).lower()}')
    i += 1
