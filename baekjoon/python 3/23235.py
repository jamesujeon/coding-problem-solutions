# 문제 링크: https://www.acmicpc.net/problem/23235

import sys

i = 0
for input in sys.stdin:
    input = input.strip()
    if input == '0':
        break

    i += 1
    print(f'Case {i}: Sorting... done!')
