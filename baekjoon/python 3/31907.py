# 문제 링크: https://www.acmicpc.net/problem/31907

K = int(input())

for _ in range(K):
    print('G' * K + '...' * K)
for _ in range(K):
    print('.' * K + 'I' * K + '.' * K + 'T' * K)
for _ in range(K):
    print('..' * K + 'S' * K + '.' * K)
