# 문제 링크: https://www.acmicpc.net/problem/23810

N = int(input())

print('\n'.join('@' * N * 5 for _ in range(N)))
print('\n'.join('@' * N for _ in range(N)))
print('\n'.join('@' * N * 5 for _ in range(N)))
print('\n'.join('@' * N for _ in range(N * 2)))
