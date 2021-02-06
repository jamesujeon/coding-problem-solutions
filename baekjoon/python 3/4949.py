# 문제 링크: https://www.acmicpc.net/problem/4949

import sys

def is_valid(s: str) -> bool:
    stack = []
    for ch in s:
        if ch in '([':
            stack.append(ch)
        elif ch in ')]':
            if len(stack) == 0 or (stack.pop() + ch) not in ('()', '[]'):
                return False
    return len(stack) == 0

while True:
    s = sys.stdin.readline()[:-1]
    if s == '.':
        break
    print('yes' if is_valid(s) else 'no')