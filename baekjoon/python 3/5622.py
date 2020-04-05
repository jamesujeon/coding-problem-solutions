# 문제 링크: https://www.acmicpc.net/problem/5622

d = ('ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')
print(sum(next(i for i, s in enumerate(d, 3) if c in s) for c in input()))
