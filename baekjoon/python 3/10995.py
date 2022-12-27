# 문제 링크: https://www.acmicpc.net/problem/10995

N = int(input())

for i in range(N):
    print((' ' if i % 2 else '') + ' '.join('*' * N))
