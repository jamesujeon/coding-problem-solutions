# 문제 링크: https://www.acmicpc.net/problem/21354

A, P = map(int, input().split())

A *= 7
P *= 13

print((('Axel', 'Petra')[A < P], 'lika')[A == P])
