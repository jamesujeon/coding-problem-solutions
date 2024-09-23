# 문제 링크: https://www.acmicpc.net/problem/11949

N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]

for i in range(2, M + 1):
    for j in range(N - 1):
        if A[j] % i > A[j + 1] % i:
            A[j], A[j + 1] = A[j + 1], A[j]

print(*A, sep='\n')
