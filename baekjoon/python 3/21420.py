# 문제 링크: https://www.acmicpc.net/problem/21420

import sys
input = sys.stdin.readline

coins = ''.join(input() for _ in range(int(input())))
print(min(coins.count('0'), coins.count('1')))
