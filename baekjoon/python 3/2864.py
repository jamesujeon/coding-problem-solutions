# 문제 링크: https://www.acmicpc.net/problem/2864

A, B = input().split()

min = lambda x: int(x.replace('6', '5'))
max = lambda x: int(x.replace('5', '6'))

print(min(A) + min(B), max(A) + max(B))
