# 문제 링크: https://www.acmicpc.net/problem/5613

import sys

result, op = 0, None
for input in sys.stdin:
    input = input.strip()
    if input == '=':
        break

    if input in '+-*/':
        op = input
    elif op:
        result = eval(f'int({result}{op}{int(input)})')
    else:
        result = int(input)

print(result)
