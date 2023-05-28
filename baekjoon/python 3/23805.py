# 문제 링크: https://www.acmicpc.net/problem/23805

N = int(input())

print('\n'.join('@@@' * N + ' ' * N + '@' * N for _ in range(N)))
print('\n'.join('@' * N + ' ' * N + '@' * N + ' ' * N + '@' * N for _ in range(N * 3)))
print('\n'.join('@' * N + ' ' * N + '@@@' * N for _ in range(N)))
