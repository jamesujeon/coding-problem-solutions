# 문제 링크: https://www.acmicpc.net/problem/16504

import sys
input = sys.stdin.readline

print(sum(sum(map(int, input().split())) for _ in range(int(input()))))
