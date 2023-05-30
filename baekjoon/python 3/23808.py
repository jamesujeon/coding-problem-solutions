# 문제 링크: https://www.acmicpc.net/problem/23808

N = int(input())

print('\n'.join('@' * N + ' ' * N * 3 + '@' * N for _ in range(N * 2)))
print('\n'.join('@' * N * 5 for _ in range(N)))
print('\n'.join('@' * N + ' ' * N * 3 + '@' * N for _ in range(N)))
print('\n'.join('@' * N * 5 for _ in range(N)))
