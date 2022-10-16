# 문제 링크: https://www.acmicpc.net/problem/6321

import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    print(f'String #{i + 1}')
    print(''.join(map(lambda x: chr((ord(x) - 64) % 26 + 65), input().strip())))
    if i < n - 1:
        print()
