# 문제 링크: https://www.acmicpc.net/problem/6436

import sys

disk_size = 62 * 30000
for i, input in enumerate(sys.stdin):
    s = int(input)
    if s == 0:
        break

    s = s / 2 + int(s % 2)
    s += s / 2
    s = int((s + disk_size - 1) / disk_size)

    print(f'File #{i + 1}')
    print(f'John needs {s} floppies.')
    print()
