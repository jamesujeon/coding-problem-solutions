# 문제 링크: https://www.acmicpc.net/problem/18698

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    print(len(input().strip().split('D')[0]))
