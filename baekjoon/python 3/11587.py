# 문제 링크: https://www.acmicpc.net/problem/11587

import sys
input = sys.stdin.readline

k = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
s = [input().strip() for _ in range(int(input()))]
d = list(map(int, input().strip()))

print(sum(all(i in k[j - 2] for i, j in zip(w, d)) for w in s))
