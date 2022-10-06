# 문제 링크: https://www.acmicpc.net/problem/5354

import sys
input = sys.stdin.readline

def print_box(size):
    print('#' * size)
    for i in range(size - 2):
        print('#' + 'J' * (size - 2) + '#')
    if size > 1:
        print('#' * size)

t = int(input())
for i in range(t):
    print_box(int(input()))
    if i < t - 1:
        print()
