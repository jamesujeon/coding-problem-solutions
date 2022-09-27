# 문제 링크: https://www.acmicpc.net/problem/3059

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    print(sum(set(range(65, 91)) - set(map(ord, input()))))
