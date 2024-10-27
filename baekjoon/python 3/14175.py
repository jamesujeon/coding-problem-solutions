# 문제 링크: https://www.acmicpc.net/problem/14175

M, N, K = map(int, input().split())
print(''.join((''.join(i * K for i in input()) + '\n') * K for _ in range(M)))
