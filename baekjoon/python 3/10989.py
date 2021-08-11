# 문제 링크: https://www.acmicpc.net/problem/10989

import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

counts = [0] * 10001
for _ in range(N):
    counts[int(input())] += 1


for i in range(10001):
    for _ in range(counts[i]):
        print(f'{i}\n')