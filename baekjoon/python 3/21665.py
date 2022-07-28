# 문제 링크: https://www.acmicpc.net/problem/21665

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
origin = [input() for _ in range(n)]
input()
output = [input() for _ in range(n)]

print(sum(origin[i][j] == output[i][j] for i in range(n) for j in range(m)))
