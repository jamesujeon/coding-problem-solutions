# 문제 링크: https://www.acmicpc.net/problem/1592

N, M, L = map(int, input().split())

i = 1
while (L * i) % N > 0:
    i += 1

print((M - 1) * i)
