# 문제 링크: https://www.acmicpc.net/problem/23809

N = int(input())

print('\n'.join('@' * N + ' ' * N * 3 + '@' * N for _ in range(N)))
print('\n'.join('@' * N + ' ' * N * 2 + '@' * N for _ in range(N)))
print('\n'.join('@' * N * 3 for _ in range(N)))
print('\n'.join('@' * N + ' ' * N * 2 + '@' * N for _ in range(N)))
print('\n'.join('@' * N + ' ' * N * 3 + '@' * N for _ in range(N)))
