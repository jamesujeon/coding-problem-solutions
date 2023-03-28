# 문제 링크: https://www.acmicpc.net/problem/18883

N, M = map(int, input().split())

print('\n'.join(' '.join(str(i * M + j) for j in range(1, M + 1)) for i in range(N)))
