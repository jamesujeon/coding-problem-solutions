# 문제 링크: https://www.acmicpc.net/problem/12813

A, B = int(input(), 2), int(input(), 2)
s = 100000
r = [A & B, A | B, A ^ B, A ^ (2**s - 1), B ^ (2**s - 1)]

print(*map(lambda x: bin(x)[2:].zfill(s), r), sep='\n')
