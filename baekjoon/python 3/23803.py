# 문제 링크: https://www.acmicpc.net/problem/23803

N = int(input())

print('\n'.join('@' * N for _ in range(N * 4)))
print('\n'.join('@' * N * 5 for _ in range(N)))
